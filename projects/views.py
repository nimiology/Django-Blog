from django.shortcuts import render, get_object_or_404
from .models import Project
from django.core.paginator import Paginator


# Create your views here.

def Projects(request, page=1):
    params = {}
    if not (request.user and request.user.is_superuser):
        params['published'] = True
    category_list = Project.objects.filter(**params).order_by('-id')
    pagintor = Paginator(category_list, 4)
    Projects = pagintor.get_page(page)
    context = {
        "projects": Projects,
    }
    return render(request, "Projects/portfolio.html", context)


def Projectgetter(request, slug):
    get_obj_params = {'slug': slug}
    if not (request.user and request.user.is_superuser):
        get_obj_params['published'] = True
    context = {
        'project': get_object_or_404(Project, **get_obj_params)
    }
    return render(request, 'Projects/portfolio-item.html', context)
