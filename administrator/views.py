from django.shortcuts import render
from website.models import JobSeeker
# Create your views here.


def index(request):
    job_seeker = JobSeeker.objects.all()
    context ={
        "job_seeker": job_seeker,
        "name":"rupesh"
    }
    return render(request, 'administrator/index.html',context)