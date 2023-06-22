from django.contrib import admin
from django.urls import path
from .views import index,about,service
urlpatterns = [
    path('',index,name="index"),
    path('about/',about,name="about-us"),
    path('service/',service,name="service"),
    path('contact-us/',about,name="contact-us")


]