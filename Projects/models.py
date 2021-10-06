from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone

# Create your models here.
from Blog.utils import slug_genrator, upload_project_picture


class Project(models.Model):
    STATUS_CHOICES = (
        ("d", "Draft"),
        ("p", "Published")
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    github = models.URLField()
    thumbnail1 = models.ImageField(upload_to=upload_project_picture, default="")
    thumbnail2 = models.ImageField(upload_to=upload_project_picture, default="")
    thumbnail3 = models.ImageField(upload_to=upload_project_picture, default="")
    text = models.TextField()
    whatIsNew = models.TextField(blank=True, null=True)
    publish = models.DateTimeField(auto_now_add=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.title


def ProjectPreSave(sender, instance, *args, **kwargs):
    if instance.slug == '':
        instance.slug = slug_genrator()


pre_save.connect(ProjectPreSave, sender=Project)
