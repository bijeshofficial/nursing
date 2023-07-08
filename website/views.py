from django.shortcuts import render

from .forms import JobSeekerForm,VacancyForm
from .models import Contact


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


def vacancy(request):
    form = VacancyForm()
    if request.method == 'POST':
        form = VacancyForm(request.POST,request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return render(request,'website/vacancy.html',{'form':form})
    return render(request,'website/vacancy.html',{'form':form})


def contact(request):
    return render(request, 'website/contact.html')

def save_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        form_data = Contact(name=name,email=email,phone_number=phone_number,subject=subject,message=message)
        form_data.save()
        
    return render(request, 'website/contact.html')
    




