from django.shortcuts import render
from .models import SocialMedias


def Home(request):
    return render(request, "StaticPages/home.html")


def SocialMedia(request):
    return render(request, "StaticPages/contact.html", {'SocialMedias': SocialMedias.objects.order_by('Title')})


def NotFound(request):
    return render(request, "StaticPages/404.html")
