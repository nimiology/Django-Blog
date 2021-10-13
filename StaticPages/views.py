from django.shortcuts import render


def Home(request):
    return render(request, "StaticPages/home.html")


def SocialMedia(request):
    return render(request, "StaticPages/contact.html")


def Error404(request, exception=None):
    context = {}
    response = render(request, "StaticPages/404.html", context=context)
    response.status_code = 404
    return response
