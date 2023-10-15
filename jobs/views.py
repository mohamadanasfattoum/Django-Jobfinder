from django.shortcuts import render
from django.views.generic import ListView
from .models import Job, Company, Categorie

class Job_list(ListView):
    model=Job
