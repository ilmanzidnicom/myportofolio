from django.urls import path

from .views import *

app_name = "AuthSSOUI"

urlpatterns = [
    path('login/', login, name='login'),
    path('callback/', callback, name='callback'),
    path('logout/', logout, name='logout'),
]
