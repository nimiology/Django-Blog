from django.shortcuts import render
from django.http import Http404
from .models import Diaries
# Create your views here.
def AllDiaries(request):
    if request.user.is_authenticated:
        context = {
            'Diaries':Diaries.objects.all()
        }
        return render(request,'Diary/All.html',context)
    raise Http404

def ADiary(request,Slug):
    if request.user.is_authenticated:
        context = {
            'Diary':Diaries.objects.get(Slug=Slug)
        }
        return render(request,'Diary/Memory.html',context)
    raise Http404
