from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Job, Company , Categorie

class JobAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(Job,JobAdmin)
admin.site.register(Company)
admin.site.register(Categorie)
