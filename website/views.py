from django.shortcuts import render

from .forms import JobSeekerForm

def index(request):
    return render(request,'website/index.html')

def about(request):
    return render(request,'website/about.html')


def service(request):
    return render(request,'website/service.html')

def job_seeker(request):
    form = JobSeekerForm()
    if request.method == 'POST':
        form = JobSeekerForm(request.POST,request.FILES)
        print(form.errors)
        if form.is_valid():
            print("it was here")
            form.save()
            return render(request,'website/job_seeker.html',{'form':form})
    return render(request,'website/job_seeker.html',{'form':form})


def contact(request):
    return render(request, 'website/contact.html')
    




