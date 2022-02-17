from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Article, Category, Tag
from django.core.paginator import Paginator


# Create your views here.
def Post(request, slug):
    get_obj_params = {'slug': slug}
    if not (request.user and request.user.is_superuser):
        get_obj_params['published'] = True
    context = {
        "article": get_object_or_404(Article, **get_obj_params),
    }
    return render(request, "Blog/blog-article.html", context)


def Blog(request, page=1):
    params = {}
    # if not (request.user and request.user.is_superuser):
    #     params['published'] = True
    article_list = Article.objects.filter(**params).order_by('-publishDate')
    search = request.GET.get('s')
    if search:
        article_list = article_list.filter(Q(title__contains=search) | Q(sections__text__contains=search))
    pagintor = Paginator(article_list, 3)
    article = pagintor.get_page(page)
    context = {
        "articles": article,
        "categories": Category.objects.filter(**params).order_by('-id')[:5],
        "tags": Tag.objects.filter(**params).order_by('-id')[:5],
        "boolean": article.number + 2 <= article.paginator.num_pages,
    }

    return render(request, "Blog/blog.html", context)


def CategoryView(request, slug, page=1):
    params = {}
    if not (request.user and request.user.is_superuser):
        params['published'] = True
    Categorys = get_object_or_404(Category, slug=slug, **params)
    article_list = Categorys.article.filter(**params)
    search = request.GET.get('s')
    if search:
        article_list = article_list.filter(Q(title__contains=search) | Q(text__contains=search))
    pagintor = Paginator(article_list, 3)
    article = pagintor.get_page(page)
    context = {
        "category": Categorys,
        "articles": article,
        "categories": Category.objects.filter(**params).order_by('-id')[:5],
        "tags": Tag.objects.filter(**params).order_by('-id')[:5],
        "boolean": article.number + 2 <= article.paginator.num_pages,

    }
    return render(request, "Blog/blog.html", context)


def TagView(request, slug, page=1):
    params = {}
    if not (request.user and request.user.is_superuser):
        params['published'] = True
    tag = get_object_or_404(Tag, slug=slug, **params)
    article_list = tag.article.filter(**params)
    search = request.GET.get('s')
    if search:
        article_list = article_list.filter(Q(title__contains=search) | Q(text__contains=search))
    pagintor = Paginator(article_list, 3)
    article = pagintor.get_page(page)
    context = {
        "category": tag,
        "articles": article,
        "categories": Category.objects.filter(**params).order_by('-id')[:5],
        "tags": Tag.objects.filter(**params).order_by('-id')[:5],
        "boolean": article.number + 2 <= article.paginator.num_pages,

    }
    return render(request, "Blog/blog.html", context)
