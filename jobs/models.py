from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

TYPY_CHOICES =(
    ('full','full'),
    ('part','part'),
    ('remote','remote'),
    ('freelance','freelance'),
)

EXPERIENCE_CHOICES =(
    ('1-2 Years','1-2 Years'),
    ('2-3 Years','2-3 Years'),
    ('3-6 Years','3-6 Years'),
    ('6-more','6-more'),
)

class Job(models.Model):
    name = models.CharField(_('Name'), max_length=120)
    image = models.ImageField(_('Image'), upload_to='job')
    job_description = models.TextField(_('Job_description'), max_length=5000, null=True, blank=True)
    rounding_salary= models.CharField(_('Rounding_salary'),max_length=50, null=True, blank=True)
    education =models.CharField(_('Education'), max_length=500, null=True, blank=True )
    experience =models.CharField(_('Experience'),max_length=100,choices=EXPERIENCE_CHOICES)
    type = models.CharField(_('Type'), max_length=10, choices=TYPY_CHOICES)
    company = models.ForeignKey('Company', verbose_name=_('Company'), related_name= 'company_jop', on_delete=models.CASCADE )
    salary= models.CharField(_('Salary'),max_length=50, null=True, blank=True )
    categorie = models.ForeignKey('Categorie', verbose_name=_('Categorie'), related_name='categorie_job', on_delete=models.CASCADE )

    def __str__(self) -> str:
        return self.name

class Company(models.Model):
    name = models.CharField(_('Name'), max_length=120)
    logo = models.ImageField(_('Logo'), upload_to='logo')
    location = models.CharField(_('Location'), max_length=120)
    company_description = models.TextField(_('Company_description'), max_length=5000, null=True, blank=True)
    web = models.CharField(_('Web'), max_length=120)
    email = models.TextField(_('Email'), max_length=500)

    def __str__(self) -> str:
        return self.name


class Categorie(models.Model):
    name = models.CharField(_('Name'), max_length=120)
    logo = models.ImageField(_('Logo'), upload_to='logo')



    def __str__(self) -> str:
        return self.name