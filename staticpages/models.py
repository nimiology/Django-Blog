from django.db import models


class Setting(models.Model):
    about = models.TextField()


class Message(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    text = models.TextField()
