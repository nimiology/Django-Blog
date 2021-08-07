from django.db import models
from django.db.models.signals import pre_save

# Create your models here.
class Diaries(models.Model):
    Text = models.TextField()
    Slug = models.SlugField(unique=True, blank=True)
    Date = models.DateTimeField(unique=True)



    def __str__(self):
        return str(self.Slug)


def Diaries_presave(sender, instance, *args, **kwargs):
    instance.Slug = instance.Date.strftime('%Y-%m-%d')


pre_save.connect(Diaries_presave, sender=Diaries)