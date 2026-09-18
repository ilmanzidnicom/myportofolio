from django.urls import path

from .views import *

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("projects/", show_projects, name="show_projects"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/add/", create_project, name="create_project"),
    path("projects/<uuid:project_id>/delete/", delete_project, name="delete_project"),
    path("api/edhistory/", get_education_history_json, name="get_education_history_json"),
    path("edhistory/add/", create_education_history, name="create_education_history"),
    path("edhistory/<uuid:edhistory_id>/update/", update_education_history, name="update_education_history"),
    path("edhistory/<uuid:edhistory_id>/delete/", delete_education_history, name="delete_education_history"),
]
