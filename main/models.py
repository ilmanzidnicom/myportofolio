import uuid
from django.db import models

# Create your models here.
class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

class EdHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    education_title = models.CharField(max_length=50)
    school = models.CharField(max_length=200)
    description = models.TextField()
    started_at_year = models.IntegerField()
    ended_at_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.education_title

    @property
    def is_ongoing(self):
        return self.ended_at_year is None
    