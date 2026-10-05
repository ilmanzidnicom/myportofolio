import requests
import xml.etree.ElementTree as ET
from urllib.parse import urlencode, quote

from django.contrib.auth import login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect
from django.urls import reverse

CAS_URL = "https://sso.ui.ac.id/cas2"

def get_callback_url(request):
    # Dynamically builds the absolute URL for the callback endpoint.
    return request.build_absolute_uri(reverse('AuthSSOUI:callback'))

def login(request):
    callback_url = get_callback_url(request)
    params = {"service": callback_url}
    login_url = f"{CAS_URL}/login?{urlencode(params)}"
    
    return redirect(login_url)

def callback(request):
    ticket = request.GET.get("ticket")
    if not ticket:
        return HttpResponseBadRequest("No ticket provided.")

    callback_url = get_callback_url(request)
    params = {
        "service": callback_url,
        "ticket": ticket
    }

    try:
        response = requests.get(
            f"{CAS_URL}/serviceValidate",
            params=params,
            timeout=10,
            headers={"User-Agent": "Mozilla/5.0"}
        )
    except requests.RequestException:
        return HttpResponse("CAS validation request failed.", status=502)

    if response.status_code != 200:
        return HttpResponse("CAS validation request failed.", status=502)

    # Parse CAS XML response
    root = ET.fromstring(response.text)
    ns = {"cas": "http://www.yale.edu/tp/cas"}

    success = root.find("cas:authenticationSuccess", ns)
    if success is None:
        return HttpResponse("Login failed. The UI SSO ticket was invalid.", status=401)

    username_node = success.find("cas:user", ns)
    username = username_node.text if username_node is not None else "unknown"

    # Fetch the existing user or automatically create a new one based on the CAS username
    user, created = User.objects.get_or_create(username=username)
    
    # Log the user into the standard Django session
    django_login(request, user)

    # Redirect to the root of website
    response = redirect(request.build_absolute_uri('/'))

    # Mark SSO
    response.set_cookie('is_sso_ui', 'true')

    return response

def logout(request):
    # Terminate the Django session first
    django_logout(request)
    
    # Redirect to the CAS server to terminate the SSO session
    base_url = request.build_absolute_uri('/')
    response = redirect(f"{CAS_URL}/logout?service={quote(base_url)}")

    # Unmark SSO
    response.delete_cookie('is_sso_ui')

    return response