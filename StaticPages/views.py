from django.shortcuts import render

from StaticPages.forms import MessageForm
from StaticPages.models import Setting, Message


def Home(request):
    return render(request, "StaticPages/home.html")


def About(request):
    messageForm = MessageForm(request.POST or None)
    context = {
        'setting': Setting.objects.all().order_by('-id')[0],
        'form': messageForm
    }
    if messageForm.is_valid():
        data = messageForm.cleaned_data
        Message(name=data['name'], email=data['email'], text=data['text']).save()

    return render(request, "StaticPages/contact.html", context=context)


def Error404(request, exception=None):
    context = {}
    response = render(request, "StaticPages/404.html", context=context)
    response.status_code = 404
    return response
