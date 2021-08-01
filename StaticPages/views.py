from django.shortcuts import render,get_object_or_404
from Blog.models import Article
from Projects.models import Project
from .models import SocialMedias
# Create your views here.

def Home(request):
    context={
        "Articleone": Article.objects.order_by("-Publish").filter(Status="p")[:1],
        "Articletwo": Article.objects.order_by("-Publish").filter(Status="p")[1:2],
        "Projects" : Project.objects.order_by("-Publish").filter(Status='p')[:1]
        }

    return render(request, "StaticPages/Home.html", context)

def SocialMedia(request):
    return render(request, "StaticPages/SocialMedia.html", {'SocialMedias':SocialMedias.objects.order_by('Title')})

