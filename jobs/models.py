from django.db import models

# Create your models here.

class Job(models.Model):
    image = models.ImageField(upload_to='jobs/static/')
    summary = models.CharField(max_length=200,default='')
    story = models.CharField(max_length=500, default='')
    title = models.CharField(max_length=50, default='')