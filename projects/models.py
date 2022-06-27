from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils import timezone

from blog.utils import slug_generator, upload_picture


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    github = models.URLField()
    thumbnail1 = models.ImageField(upload_to=upload_picture, default="")
    thumbnail2 = models.ImageField(upload_to=upload_picture, default="")
    thumbnail3 = models.ImageField(upload_to=upload_picture, default="")
    text = models.TextField()
    publishDate = models.DateTimeField(auto_now_add=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('projects:project', args=(self.slug,))


def ProjectPreSave(sender, instance, *args, **kwargs):
    if instance.slug == '':
        instance.slug = slug_generator(5)


pre_save.connect(ProjectPreSave, sender=Project)
