from django.shortcuts import render, get_object_or_404
from .models import Article, Category, Tag
from django.core.paginator import Paginator


# Create your views here.
def Post(request, slug):
    context = {
        "article": get_object_or_404(Article, slug=slug, published=True),
    }
    return render(request, "Blog/blog-article.html", context)


def Blog(request, page=1):
    article_list = Article.objects.filter(published=True)
    pagintor = Paginator(article_list, 3)
    article = pagintor.get_page(page)
    context = {
        "articles": article,
        "categories": Category.objects.filter(status=True).order_by('-id')[:5],
        "tags": Tag.objects.filter(status=True).order_by('-id')[:5]
    }

    return render(request, "Blog/blog.html", context)


def CategoryView(request, slug, page=1):
    Categorys = get_object_or_404(Category, slug=slug, status=True)
    article_list = Categorys.article.filter(published=True)
    pagintor = Paginator(article_list, 6)
    article = pagintor.get_page(page)
    context = {
        "category": Categorys,
        "articles": article,
        "categories": Category.objects.filter(status=True).order_by('-id')[:5],
        "tags": Tag.objects.filter(status=True).order_by('-id')[:5]
    }
    return render(request, "Blog/blog.html", context)


def TagView(request, slug, page=1):
    tag = get_object_or_404(Tag, slug=slug, status=True)
    article_list = tag.article.filter(published=True)
    pagintor = Paginator(article_list, 6)
    article = pagintor.get_page(page)
    context = {
        "category": tag,
        "articles": article,
        "categories": Category.objects.filter(status=True).order_by('-id')[:5],
        "tags": Tag.objects.filter(status=True).order_by('-id')[:5]
    }
    return render(request, "Blog/blog.html", context)