from django.contrib import messages
from django.shortcuts import redirect, render

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
    context = {
        "project_list": Project.objects.all(),
    }
    return render(request, "project.html", global_context | context)

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