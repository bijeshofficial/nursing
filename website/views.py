from django.shortcuts import render

from .forms import JobSeekerForm,VacancyForm
from .models import Contact,Service,JobPost
from django.shortcuts import get_object_or_404



def index(request):
    return render(request,'website/index.html')

def about(request):
    return render(request,'website/about.html')


def service(request):
    return render(request,'website/service.html')


def homecare(request):
    home_care = Service.objects.get(title="Home Care")
    points = home_care.points.all()
    context = {
        "home_care": home_care,
        "points": points
    }
    return render(request,'website/homecare.html',context)

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

def training(request):
    home_care = get_object_or_404(Service,title="Training")

    points = home_care.points.all()
    context = {
        "home_care": home_care,
        "points": points
    }
    return render(request,'website/training.html',context)



def aged_care(request):
    home_care = get_object_or_404(Service,title="Aged Care")

    points = home_care.points.all()
    context = {
        "home_care": home_care,
        "points": points
    }
    return render(request,'website/aged_care.html',context)



def find_jobs(request):
    listed_jobs = JobPost.objects.all()
    context = {
        "jobs":listed_jobs
    }
    return render(request,'website/find_job.html',context)

def job_detail(request,pk):
    job = get_object_or_404(JobPost,pk=pk)
    print(job.content)
    context = {
        "job":job
    }
    return render(request,'website/job_detail.html',context)


def disability_support(request):
    home_care = get_object_or_404(Service,title="Disability Support")

    points = home_care.points.all()
    context = {
        "home_care": home_care,
        "points": points
    }
    return render(request,'website/disability_support.html',context)


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
    




