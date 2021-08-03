from django.shortcuts import render,get_object_or_404
from .models import Project
from django.core.paginator import Paginator

# Create your views here.

def Projects(request,page=1):
    category_list = Project.objects.filter()
    pagintor = Paginator(category_list, 4)
    Projects = pagintor.get_page(page)
    #Projects = Projects.order_by("-Publish")
    context = {
        "Projects" : Projects,
        "Projectone": Projects[:1],
    }
    return render(request, "Projects/Projects.html", context)

def Projectgetter(request,slug):
    context = {
        'Project' : get_object_or_404(Project, slug=slug,Status='p')
    }
    return render(request, 'Projects/Project.html', context)