from django.contrib import admin

from .models import JobSeeker,Qualification,Position


admin.site.register(JobSeeker)
admin.site.register(Qualification)
admin.site.register(Position)