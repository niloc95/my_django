from django.db import models


class Job(models.Model):
    image = models.ImageField(upload_to='mypersonal/static/images')
    summary = models.CharField(max_length=200)
# Create your models here.
