from django.shortcuts import render
from app.models import *
from django.views.generic import ListView,DetailView
from django.http import HttpResponse
# Create your views here.
class SchoolList(ListView):
    model=School
    context_object_name='schools'
    #queryset=School.objects.filter(Sname='Qspiders')
    #ordering=['Sname']



def wish(request,n):
    return HttpResponse(f'Hai {n} How R U')


class SchoolDetail(DetailView):
    model=School
    context_object_name='schoolobject'
    #template_name='app/school_detail.html'
