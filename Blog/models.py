from django.db import models
from django.utils import timezone

# Create your models here.
class ArticleManager(models.Manager):
    def Published(self):
        return self.filter(Status='p')

class Category(models.Model):

    Title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    Status = models.BooleanField(default=True)
    Position = models.IntegerField()

    class Meta:
        ordering = ['Position']

    def __str__(self):
        return self.Title


class Article(models.Model):
    STATUS_CHOICES = (
        ("d","Draft"),
        ("p","Published")
    )
    Title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    Text = models.TextField()
    Category = models.ManyToManyField(Category,related_name="Article")
    Thumbnail = models.ImageField(upload_to="Images")
    Publish = models.DateTimeField(default=timezone.now)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    Status = models.CharField(max_length=1,choices=STATUS_CHOICES)
    class Meta:
        ordering = ['-Publish']

    def __str__(self):
        return self.Title

    def category_Publish(self):
        return self.Category.filter(Status=True)

    objects = ArticleManager()
