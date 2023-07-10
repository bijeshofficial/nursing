from django.contrib import admin
from django.urls import path
from .views import index, about, service, job_seeker, contact, save_contact,vacancy,training,homecare,disability_support,aged_care
urlpatterns = [
    path('',index,name="index"),
    # path('home',index, name="home"),
    path('about/',about,name="about-us"),
    path('service/',service,name="service"),
    path('homecare/',homecare,name="home-care"),
    path('job-seeker/',job_seeker,name="job-seeker"),
    path('training/',training,name="training"),
    path('disability-support/',disability_support,name="disability-support"),
    path('aged-care/',aged_care,name="aged-care"),
    path('contact', contact, name = "contact-us"),
    path('save-contact', save_contact, name="save-contact"),
     path('vacancy', vacancy, name="vacancy")
    


]