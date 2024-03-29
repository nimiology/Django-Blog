from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils import timezone

from blog.utils import slug_generator, upload_picture


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:category', args=(self.slug,))


class Tag(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:tag', args=(self.slug,))


class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    categories = models.ManyToManyField(Category, blank=True, related_name="article")
    tags = models.ManyToManyField(Tag, blank=True, related_name="article")
    thumbnail = models.ImageField(upload_to=upload_picture, null=True, blank=True)
    writer = models.CharField(max_length=200, default='Nima')
    publishDate = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def category_Publish(self):
        return self.categories.filter(Status=True)

    def preview_text(self):
        qs = self.sections.all()
        if qs.exists():
            return qs[0].text
        return ''

    def get_absolute_url(self):
        return reverse('blog:article', args=(self.slug,))


class Section(models.Model):
    related_name = 'sections'

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name=related_name)
    title = models.CharField(max_length=200, null=True, blank=True)
    picture = models.ImageField(upload_to=upload_picture, blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    text = models.TextField(null=True, blank=True)
    code = models.TextField(null=True, blank=True)
    position = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.article.title} - {self.position}'

    class Meta:
        ordering = ['article', 'position', 'id']

    def get_absolute_url(self):
        return reverse('blog:article', args=(self.article.slug,))


def ArticlePreSave(sender, instance, *args, **kwargs):
    if instance.slug == '':
        instance.slug = slug_generator(5)


def section_pre_save(sender, instance, *args, **kwargs):
    if instance.position is None:
        project_sections = sender.objects.filter(article=instance.article).order_by('-position')
        if project_sections.exists():
            project_section = project_sections[0]
            instance.position = project_section.position + 1
        else:
            instance.position = 0


pre_save.connect(ArticlePreSave, sender=Article)
pre_save.connect(section_pre_save, sender=Section)
