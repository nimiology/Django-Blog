from django.db import models

# Create your models here.
class SocialMedias(models.Model):
    Title = models.CharField(max_length=200)
    Link = models.TextField()