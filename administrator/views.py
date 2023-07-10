from django.shortcuts import render
from website.models import JobSeeker,Qualification,Position,Contact,Service
from .forms import PositionForm,QualificationForm
from django.shortcuts import redirect

def index(request):
    job_seeker = JobSeeker.objects.all()
    context ={
        "job_seeker": job_seeker,
        "name":"rupesh"
    }
    return render(request, 'administrator/admin_index.html',context)



def qualification_dashboard(request): 
    qualifications = Qualification.objects.all()
    context = {
        "qualifications":qualifications
    }

    return render(request, 'administrator/qualification.html',context)

def contact_listing(request): 
    contacts = Contact.objects.all()
    context = {
        "contacts":contacts
    }

    return render(request, 'administrator/contact.html',context)



def pages(request): 
    pages = Service.objects.all()
    print(pages)
    context = {
        "pages":pages
    }

    return render(request, 'administrator/pages.html',context)



def seeker(request): 
    seekers = JobSeeker.objects.all()
    context = {
        "seekers":seekers
    }

    return render(request, 'administrator/seeker.html',context)

def create_position(request): 
    form = PositionForm()
    if request.method == 'POST':
        form = PositionForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('position-dashboard')
    return render(request,'administrator/create_position.html',{'form':form})


def create_qualification(request): 
    form = QualificationForm()
    if request.method == 'POST':
        form = QualificationForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('qualification-dashboard')
    return render(request,'administrator/create_qualification.html',{'form':form})



def update_qualification(request,pk):
    data = Qualification.objects.get(pk=pk)
    form = QualificationForm(instance = data)
    if request.method == "POST": 
        form = QualificationForm(request.POST,instance = data)
        if form.is_valid():
            form.save()
            return redirect('qualification-dashboard')
    else: 
        context = {
            'form':form
        }

    return render(request,'administrator/update_qualification.html',context)



def update_position(request,pk):
    data = Position.objects.get(pk=pk)
    form = PositionForm(instance = data)
    if request.method == "POST": 
        form = PositionForm(request.POST,instance = data)
        if form.is_valid():
            form.save()
            return redirect('position-dashboard')
    else: 
        context = {
            'form':form
        }

    return render(request,'administrator/update_position.html',context)    


def delete_qualification(request,pk):
    data = Qualification.objects.get(pk=pk)
    data.delete()
    return redirect('qualification-dashboard')
    


def delete_position(request,pk):
    data = Position.objects.get(pk=pk)
    data.delete()
    return redirect('position-dashboard')

def position_dashboard(request): 
    positions = Position.objects.all()
    context = {
        "positions":positions
    }

    return render(request, 'administrator/position.html',context)


