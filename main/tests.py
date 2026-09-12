from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import *

# Create your tests here.
class AvailabilityTest(TestCase):
    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

class EducationHistoryTest(TestCase):
    def setUp(self):
        self.EdHistory1 = EdHistory.objects.create(
            education_title="Elementry School",
            school="SD Islam Al-Azhar 6 Jakapermai",
            description="I got inspired to do computer programming from Roblox LUA.",
            started_at_year=2011,
            ended_at_year=2018,
        )
        self.EdHistory2 = EdHistory.objects.create(
            education_title="College",
            school="Universitas Indonesia, Faculty of Computer Science",
            description="Here I am today!",
            started_at_year=2025,
        )

    def test_edhistory_model(self):
        self.assertEqual(str(self.EdHistory1), "Elementry School")
        self.assertEqual(self.EdHistory1.school, "SD Islam Al-Azhar 6 Jakapermai")
        self.assertEqual(self.EdHistory1.description, "I got inspired to do computer programming from Roblox LUA.")
        self.assertEqual(self.EdHistory1.started_at_year, 2011)
        self.assertEqual(self.EdHistory1.ended_at_year, 2018)
        self.assertFalse(self.EdHistory1.is_ongoing)

        self.assertEqual(str(self.EdHistory2), "College")
        self.assertEqual(self.EdHistory2.school, "Universitas Indonesia, Faculty of Computer Science")
        self.assertEqual(self.EdHistory2.description, "Here I am today!")
        self.assertEqual(self.EdHistory2.started_at_year, 2025)
        self.assertTrue(self.EdHistory2.is_ongoing)

    def test_edhistory_page(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

        self.assertContains(response, self.EdHistory1.education_title)
        self.assertContains(response, self.EdHistory1.school)
        self.assertContains(response, self.EdHistory1.description)
        self.assertContains(response, self.EdHistory1.started_at_year)
        self.assertContains(response, self.EdHistory1.ended_at_year)

        self.assertContains(response, self.EdHistory2.education_title)
        self.assertContains(response, self.EdHistory2.school)
        self.assertContains(response, self.EdHistory2.description)
        self.assertContains(response, self.EdHistory2.started_at_year)
        self.assertContains(response, "Present")

    def test_empty_edhistory_page(self):
        EdHistory.objects.all().delete()
        response = self.client.get(reverse("main:show_main"))

        self.assertContains(response, "Belum ada data.")

class ExperienceTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")