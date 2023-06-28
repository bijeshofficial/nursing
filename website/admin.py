from django.contrib import admin

from .models import JobSeeker,Qualification,Position, Contact,Vacancy


admin.site.register(JobSeeker)
admin.site.register(Qualification)
admin.site.register(Position)
admin.site.register(Contact)
admin.site.register(Vacancy)