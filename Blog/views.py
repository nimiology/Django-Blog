from django.shortcuts import render,get_object_or_404
from .models import Article,Category
from django.core.paginator import Paginator
# Create your views here.
def Blog(request, slug):
    context={
        "Article": get_object_or_404(Article, slug=slug,Status='p')
    }
    return render(request, "Blog/Post.html", context)

def articles(request , page=1):
    article_list = Article.objects.Published()
    pagintor = Paginator(article_list, 6)
    article = pagintor.get_page(page)
    context={
        "Articles": article
        }

    return render(request, "Blog/Blog.html", context)

def Categorygetter(request,slug, page=1):
    Categorys = get_object_or_404(Category, slug=slug,Status=True)
    article_list = Categorys.Article.Published()
    pagintor = Paginator(article_list, 6)
    article = pagintor.get_page(page)
    context={
        "Category": Categorys,
        "Articles": article
        }
    return render(request,"Blog/Category.html",context)