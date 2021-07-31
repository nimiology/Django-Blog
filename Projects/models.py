from django.db import models
from django.utils import timezone
# Create your models here.
class Project(models.Model):
    STATUS_CHOICES = (
        ("d","Draft"),
        ("p","Published")
    )
    Title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    Github = models.TextField()
    Thumbnail = models.ImageField(upload_to="Images",default="")
    Text = models.TextField()
    Publish = models.DateTimeField(auto_now_add=timezone.now)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    Status = models.CharField(max_length=1,choices=STATUS_CHOICES)
    class Meta:
        ordering = ['-Publish']
    def __str__(self):
        return self.Title