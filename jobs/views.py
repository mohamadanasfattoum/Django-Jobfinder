from django.shortcuts import render
from django.views import generic
from .models import Job, Company, Categorie

class Job_list(generic.ListView):
    model=Job
