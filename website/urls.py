from django.contrib import admin
from django.urls import path
from .views import index,about,service,job_seeker
urlpatterns = [
    path('',index,name="index"),
    path('about/',about,name="about-us"),
    path('service/',service,name="service"),
    path('job-seeker/',job_seeker,name="job-seeker"), 
    


]