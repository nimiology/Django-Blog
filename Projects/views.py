from django.shortcuts import render, get_object_or_404
from .models import Project
from django.core.paginator import Paginator


# Create your views here.

def Projects(request, page=1):
    category_list = Project.objects.filter(publish=True).order_by('-id')
    pagintor = Paginator(category_list, 4)
    Projects = pagintor.get_page(page)
    context = {
        "projects": Projects,
    }
    return render(request, "Projects/portfolio.html", context)


def Projectgetter(request, slug):
    context = {
        'project': get_object_or_404(Project, slug=slug, publish=True)
    }
    return render(request, 'Projects/portfolio-item.html', context)
