from django.shortcuts import render

from staticpages.forms import HomeMessageForm, ContactMessageForm
from staticpages.models import Setting, Message
from projects.models import Project


def Home(request):
    messageForm = HomeMessageForm(request.POST or None)
    if messageForm.is_valid():
        data = messageForm.cleaned_data
        Message.objects.create(name=data['name'], email=data['email'], text=data['text'])
        messageForm = HomeMessageForm()
    context = {
        'project': Project.objects.all().order_by('-id').first,
        'form': messageForm,
    }
    return render(request, "StaticPages/home.html", context=context)


def contact(request):
    messageForm = ContactMessageForm(request.POST or None)
    if messageForm.is_valid():
        data = messageForm.cleaned_data
        Message.objects.create(name=data['name'], email=data['email'], text=data['text'])
        messageForm = HomeMessageForm()
    context = {
        'form': messageForm
    }
    return render(request, "StaticPages/contact.html", context=context)


def error404(request, exception=None):
    context = {}
    response = render(request, "StaticPages/404.html", context=context)
    response.status_code = 404
    return response


def faq(request):
    return render(request, "StaticPages/faq.html")


def process(request):
    return render(request, "StaticPages/process.html")


def about(request):
    return render(request, "StaticPages/about.html")
