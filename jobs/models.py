from django.db import models

# Create your models here.

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    story = models.CharField(max_length=500)
    title = models.CharField(max_length=50)