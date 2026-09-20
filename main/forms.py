from django.forms import ModelForm, TextInput, Textarea, URLInput, NumberInput

from .models import *

class EdHistoryForm(ModelForm):
    class Meta:
        model = EdHistory
        fields = [
            "education_title",
            "school",
            "description",
            "started_at_year",
            "ended_at_year",
        ]

        labels = {
            "education_title": "Education Title",
            "school": "School",
            "description": "Description",
            "started_at_year": "Started at Year",
            "ended_at_year": "Ended at Year",
        }

        widgets = {
            "education_title": TextInput(
                attrs={
                    "placeholder": "High School",
                    "maxlength": 50,
                }
            ),
            "school": TextInput(
                attrs={
                    "placeholder": "SMAN 8 Bekasi",
                    "maxlength": 200,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan pengalamanmu.",
                    "rows": 3,
                }
            ),
            "started_at_year": NumberInput(
                attrs={
                    "placeholder": 2010
                }
            ),
            "ended_at_year": NumberInput(
                attrs={
                    "placeholder": 2015
                }
            ),
        }

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Project",
            "description": "Deskripsi Project",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Project",
            "project_image_url": "URL Gambar Project",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Projectmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }