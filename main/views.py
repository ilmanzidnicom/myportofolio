from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.core.exceptions import PermissionDenied 
from datetime import datetime
from zoneinfo import ZoneInfo
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q

from .models import *
from .forms import *

global_context = {
    "name": "Ilman Zidni",
}

# Create your views here.
def show_main(request):
    education_year_query = request.GET.get("education-year", "").strip()
    last_login = request.COOKIES.get('last_login')

    context = {
        "npm": "2506621951",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Hi there! My name is Ilman Zidni. I love computers, and I’m currently a student of Universitas Indonesia in Fasilkom! I’m always striving to learn new and exciting things about computers and technology. I love tackling projects, from building websites to tinkering with new programming languages and frameworks, because I learn best by trial and error. I enjoy sharing what I’ve learned with others, whether that’s helping a friend with their computer problems or contributing to projects."
        ),
        "last_login": last_login,
        "education_year_query": education_year_query,
        "form": EdHistoryForm(),
    }
    return render(request, "home.html", global_context | context)


def show_experience(request):
    context = {
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", global_context | context)

def show_projects(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "title_query": title_query,
        "form": ProjectForm(),
    }
    return render(request, "project.html", global_context | context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.prefetch_related('starred_by').all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    # Konstruksi data JSON secara manual agar bisa menyisipkan logika Star
    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "tech_stack": project.tech_stack,
                "project_url": project.project_url,
                "project_image_url": project.project_image_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.has_perm("main.add_project"):
        raise PermissionDenied

    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Project baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "form": form,
        "page_title": "Add New Project",
        "post_form_url": reverse("main:create_project"),
        "submit_button_text": "Add Project",
        "cancel_button_url": reverse("main:show_projects"),
    }

    return render(request, "form.html", global_context | context)

@require_POST
def create_project_ajax(request):
    if not request.user.has_perm("main.add_project"):
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan proyek."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Proyek berhasil ditambahkan.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.has_perm("main.delete_project"):
        raise PermissionDenied

    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")

def get_education_history_json(request):
    education_year_query = request.GET.get("education-year", "").strip()
    all_education_history = EdHistory.objects.all()

    if education_year_query:
        all_education_history = all_education_history\
                                .filter(started_at_year__lte=education_year_query)\
                                .filter(Q(ended_at_year__gte=education_year_query) | Q(ended_at_year__isnull=True))

    # Konstruksi data JSON secara manual
    data = []
    for edhistory in all_education_history:
        data.append({
            "pk": str(edhistory.id),
            "fields": {
                "education_title": edhistory.education_title,
                "school": edhistory.school,
                "description": edhistory.description,
                "started_at_year": edhistory.started_at_year,
                "ended_at_year": edhistory.ended_at_year,
            }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
def create_education_history(request):
    if not request.user.has_perm("main.add_edhistory"):
        raise PermissionDenied

    form = EdHistoryForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Project baru berhasil ditambahkan!")
        return redirect("main:show_main")

    context = {
        "form": form,
        "page_title": "Add New Education",
        "post_form_url": reverse("main:create_education_history"),
        "submit_button_text": "Add Education",
        "cancel_button_url": reverse("main:show_main"),
    }

    return render(request, "form.html", global_context | context)

@require_POST
def create_education_history_ajax(request):
    if not request.user.has_perm("main.add_edhistory"):
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan Education History."},
            status=403,
        )

    form = EdHistoryForm(request.POST)
    if form.is_valid():
        edhistory = form.save()
        return JsonResponse(
            {"message": "Education History berhasil ditambahkan.", "pk": str(edhistory.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

@login_required(login_url="/login/")
def update_education_history(request, edhistory_id):
    if not request.user.has_perm("main.change_edhistory"):
        raise PermissionDenied

    edhistory = get_object_or_404(EdHistory, pk=edhistory_id)

    form = EdHistoryForm(request.POST or None, instance=edhistory)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Project berhasil diupdate!")
        return redirect("main:show_main")

    context = {
        "form": form,
        "page_title": "Update Education",
        "post_form_url": reverse("main:update_education_history", kwargs={"edhistory_id": edhistory_id}),
        "submit_button_text": "Update Education",
        "cancel_button_url": reverse("main:show_main"),
    }

    return render(request, "form.html", global_context | context)

@login_required(login_url="/login/")
def delete_education_history(request, edhistory_id):
    if not request.user.has_perm("main.delete_edhistory"):
        raise PermissionDenied
    
    edhistory = get_object_or_404(EdHistory, pk=edhistory_id)

    if request.method == "POST":
        edhistory.delete()
        messages.success(request, "Education berhasil dihapus!")
        return redirect("main:show_main")

    return redirect("main:show_main")

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "form": form,
    }
    return render(request, "register.html", global_context | context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())

        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.now(ZoneInfo("Asia/Jakarta")).strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "form": form,
    }
    return render(request, "login.html", global_context | context)

def logout_user(request):
    logout(request)

    response = redirect("main:show_main")

    if (request.COOKIES.get('is_sso_ui') == 'true'):
        response = redirect("AuthSSOUI:logout")
    
    response.delete_cookie('last_login')

    return response