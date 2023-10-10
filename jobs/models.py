from django.db import models

TYPY_CHOICES =(
    ('full','full'),
    ('part','part'),
    ('remote','remote'),
    ('freelance','freelance'),
)
class Job(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='job')
    logo = models.ImageField(upload_to='logo')
    salary= models.FloatField()
    type = models.CharField(max_length=10, choices=TYPY_CHOICES)
    company = models.ForeignKey('Company', related_name= 'company_jop', on_delete=models.SET_NULL, null=True, blank=True)

class Company(models.Model):
    name = models.CharField(max_length=120)
    logo = models.ImageField(upload_to='logo')
    salary= models.FloatField()
    location = models.CharField(max_length=120)
    description = models.TextField(max_length=5000)
    web = models.CharField(max_length=120)
    email = models.TextField(max_length=500)

