from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone

from Blog.utils import slug_genrator, upload_project_picture


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    github = models.URLField()
    thumbnail1 = models.ImageField(upload_to=upload_project_picture, default="")
    thumbnail2 = models.ImageField(upload_to=upload_project_picture, default="")
    thumbnail3 = models.ImageField(upload_to=upload_project_picture, default="")
    text = models.TextField()
    publishDate = models.DateTimeField(auto_now_add=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.BooleanField()

    def __str__(self):
        return self.title


def ProjectPreSave(sender, instance, *args, **kwargs):
    if instance.slug == '':
        instance.slug = slug_genrator()


pre_save.connect(ProjectPreSave, sender=Project)
