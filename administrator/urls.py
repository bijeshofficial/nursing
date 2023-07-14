from django.contrib import admin
from django.urls import path
from .views import index, qualification_dashboard,create_qualification,update_qualification,delete_qualification,position_dashboard,create_position,update_position,delete_position,contact_listing,seeker,pages,login_user,create_job,listing_jobs,logout_user,update_job,delete_job
urlpatterns = [

#'''
# Below path for dashboard
# ''' 

    path('',index,name="admin_index"),


#'''
# Below paths are used to create,delete,update and list new Qualification
# ''' 

     path('qualification-dashboard/',qualification_dashboard,name="qualification-dashboard"),
       path('qualification-create/',create_qualification,name="qualification-create"),
       path("update-qualification/<int:pk>/",update_qualification,name="update_qualification"),
        path("delete-qualification/<int:pk>/",delete_qualification,name="delete_qualification"),


#'''
# Below paths are used to create,delete,update and list new Position
# ''' 

      path('position-dashboard/',position_dashboard,name="position-dashboard"),
       path('position-create/',create_position,name="position-create"),
       path("update-position/<int:pk>/",update_position,name="update_position"),
        path("delete-position/<int:pk>/",delete_position,name="delete_position"),


#'''
# Below list contact 
# ''' 
path('contact-list/',contact_listing,name="contact-list"),


#'''
# Below list pages
# ''' 
path('pages/',pages,name="pages"),


#'''
# Below list seeker application
# ''' 
path('seekers/',seeker,name="seeker"),
        

#'''
# Below logout and login users
# ''' 
path('login/',login_user,name="login"),
path('logout/',logout_user,name="logout"),

         
#'''
# Below paths are used to create,delete,update and list new Job Listing
# ''' 
    path('create-job-vacancy/',create_job,name="create-job-vacancy"),
    path('listed-jobs/',listing_jobs,name="listed-job"),
   path("job/<int:pk>/",update_job,name="update-job"),
   path("job/delete/<int:pk>/",delete_job,name="delete-job"),

    
]