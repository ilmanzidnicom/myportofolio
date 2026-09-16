from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import *
from .forms import *

global_context = {
    "name": "Ilman Zidni",
}

# Create your views here.
def show_main(request):
    context = {
        "npm": "2506621951",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Hi there! My name is Ilman Zidni. I love computers, and I’m currently a student of Universitas Indonesia in Fasilkom! I’m always striving to learn new and exciting things about computers and technology. I love tackling projects, from building websites to tinkering with new programming languages and frameworks, because I learn best by trial and error. I enjoy sharing what I’ve learned with others, whether that’s helping a friend with their computer problems or contributing to projects."
        ),
        "all_education_history": EdHistory.objects.all(),
    }
    return render(request, "home.html", global_context | context)


def show_experience(request):
    context = {
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", global_context | context)

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", global_context | context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "form": form,
    }

    return render(request, "projects_form.html", global_context | context)

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")