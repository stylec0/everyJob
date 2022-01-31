from django.contrib import admin

# Register your models here.

from .models import JobPost, JobTitle

admin.site.register(JobPost)
admin.site.register(JobTitle)
