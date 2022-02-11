from django.shortcuts import render

from staticpages.forms import MessageForm
from staticpages.models import Setting, Message


def Home(request):
    return render(request, "StaticPages/home.html")


def About(request):
    messageForm = MessageForm(request.POST or None)
    if messageForm.is_valid():
        data = messageForm.cleaned_data
        Message.objects.create(name=data['name'], email=data['email'], text=data['text'])
        messageForm = MessageForm()
    context = {
        'setting': Setting.objects.all().order_by('-id')[0],
        'form': messageForm
    }
    return render(request, "StaticPages/contact.html", context=context)


def Error404(request, exception=None):
    context = {}
    response = render(request, "StaticPages/404.html", context=context)
    response.status_code = 404
    return response
