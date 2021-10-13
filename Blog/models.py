from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone

from Blog.utils import slug_genrator, upload_project_picture


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    text = models.TextField()
    categories = models.ManyToManyField(Category, related_name="article")
    thumbnail = models.ImageField(upload_to=upload_project_picture)
    writer = models.CharField(max_length=200, default='Nima')
    publishDate = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField()

    def __str__(self):
        return self.title

    def category_Publish(self):
        return self.categories.filter(Status=True)


def ArticlePreSave(sender, instance, *args, **kwargs):
    if instance.slug == '':
        instance.slug = slug_genrator()


pre_save.connect(ArticlePreSave, sender=Article)
