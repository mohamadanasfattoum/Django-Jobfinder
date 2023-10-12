from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

TYPY_CHOICES =(
    ('full','full'),
    ('part','part'),
    ('remote','remote'),
    ('freelance','freelance'),
)
class Job(models.Model):
    name = models.CharField(_('Name'), max_length=120)
    image = models.ImageField(_('Image'), upload_to='job')
    logo = models.ImageField(_('Logo'), upload_to='logo')
    job_description = models.TextField(_('Job_description'), max_length=5000, null=True, blank=True)
    rounding_salary= models.CharField(_('Rounding_salary'),max_length=50, null=True, blank=True)
    education =models.CharField(_('Education'), max_length=500, null=True, blank=True )
    experience =models.CharField(_('Experience'), max_length=500, null=True, blank=True)
    type = models.CharField(_('Type'), max_length=10, choices=TYPY_CHOICES)
    company = models.ForeignKey('Company', verbose_name=_('Company'), related_name= 'company_jop', on_delete=models.SET_NULL, null=True, blank=True)


class Company(models.Model):
    name = models.CharField(_('Name'), max_length=120)
    logo = models.ImageField(_('Logo'), upload_to='logo')
    salary= models.CharField(_('Salary'),max_length=50, null=True, blank=True )
    location = models.CharField(_('Location'), max_length=120)
    company_description = models.TextField(_('Company_description'), max_length=5000, null=True, blank=True)
    web = models.CharField(_('Web'), max_length=120)
    email = models.TextField(_('Email'), max_length=500)



class Categorie(models.Model):
    name = models.CharField(_('Name'), max_length=120)
    job = models.ForeignKey(Job, related_name='categorie_job', on_delete=models.CASCADE ) 
    logo = models.ImageField(_('Logo'), upload_to='logo')
    count = models.IntegerField(_('count'), null=True, blank=True)