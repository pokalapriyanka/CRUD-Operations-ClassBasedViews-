from django.shortcuts import render
from app.models import *
from django.views.generic import ListView,DetailView,TemplateView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
# Create your views here.

class Home(TemplateView):
    template_name='app/home.html'


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

class SchoolCreate(CreateView):
    model=School
    fields='__all__'

class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'

class SchoolDelete(DeleteView):
    model=School
    context_object_name='schoolobj'
    success_url=reverse_lazy('SchoolList')