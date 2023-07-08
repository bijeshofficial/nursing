from django.contrib import admin
from django.urls import path
from .views import index, qualification_dashboard,create_qualification,update_qualification,delete_qualification,position_dashboard,create_position,update_position,delete_position,contact_listing,seeker
urlpatterns = [
    path('',index,name="admin_index"),
     path('qualification-dashboard/',qualification_dashboard,name="qualification-dashboard"),
       path('qualification-create/',create_qualification,name="qualification-create"),
       path("update-qualification/<int:pk>/",update_qualification,name="update_qualification"),
        path("delete-qualification/<int:pk>/",delete_qualification,name="delete_qualification"),





      path('position-dashboard/',position_dashboard,name="position-dashboard"),
       path('position-create/',create_position,name="position-create"),
       path("update-position/<int:pk>/",update_position,name="update_position"),
        path("delete-position/<int:pk>/",delete_position,name="delete_position"),


        path('contact-list/',contact_listing,name="contact-list"),



        path('seekers/',seeker,name="seeker"),


]