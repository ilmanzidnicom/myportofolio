from django.shortcuts import render

from main.models import Experience

# Create your views here.
def show_main(request):
    context = {
        "name": "Ilman Zidni",
        "npm": "2506621951",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Hi there! My name is Ilman Zidni. I love computers, and I’m currently a student of Universitas Indonesia in Fasilkom! I’m always striving to learn new and exciting things about computers and technology. I love tackling projects, from building websites to tinkering with new programming languages and frameworks, because I learn best by trial and error. I enjoy sharing what I’ve learned with others, whether that’s helping a friend with their computer problems or contributing to projects."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Ilman Zidni",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)