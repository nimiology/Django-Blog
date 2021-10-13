from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from django.core.paginator import Paginator


# Create your views here.
def Blog(request, slug):
    context = {
        "article": get_object_or_404(Article, slug=slug, published=True)
    }
    return render(request, "Blog/blog-article.html", context)


def articles(request, page=1):
    article_list = Article.objects.filter(published=True)
    pagintor = Paginator(article_list, 3)
    article = pagintor.get_page(page)
    context = {
        "articles": article
    }

    return render(request, "Blog/Blog.html", context)


def Categorygetter(request, slug, page=1):
    Categorys = get_object_or_404(Category, slug=slug, status=True)
    article_list = Categorys.article.filter(published=True)
    pagintor = Paginator(article_list, 6)
    article = pagintor.get_page(page)
    context = {
        "category": Categorys,
        "articles": article
    }
    return render(request, "Blog/blog.html", context)
