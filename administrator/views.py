from django.shortcuts import render
from website.models import JobSeeker,Qualification,Position,Contact,Service,JobPost
from .forms import PositionForm,QualificationForm,JobPostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


@login_required
def index(request):
    job_seeker = JobSeeker.objects.all()
    context ={
        "job_seeker": job_seeker,
        "name":"rupesh"
    }
    return render(request, 'administrator/admin_index.html',context)




@login_required
def logout_user(request):
    logout(request)
    return redirect("login")


@login_required
def qualification_dashboard(request): 
    qualifications = Qualification.objects.all()
    context = {
        "qualifications":qualifications
    }

    return render(request, 'administrator/qualification.html',context)


@login_required
def contact_listing(request): 
    contacts = Contact.objects.all()
    context = {
        "contacts":contacts
    }

    return render(request, 'administrator/contact.html',context)


@login_required
def pages(request): 
    pages = Service.objects.all()
    print(pages)
    context = {
        "pages":pages
    }

    return render(request, 'administrator/pages.html',context)


@login_required
def seeker(request): 
    seekers = JobSeeker.objects.all()
    context = {
        "seekers":seekers
    }

    return render(request, 'administrator/seeker.html',context)


@login_required
def create_position(request): 
    form = PositionForm()
    if request.method == 'POST':
        form = PositionForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('position-dashboard')
    return render(request,'administrator/create_position.html',{'form':form})

@login_required
def create_qualification(request): 
    form = QualificationForm()
    if request.method == 'POST':
        form = QualificationForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('qualification-dashboard')
    return render(request,'administrator/create_qualification.html',{'form':form})


@login_required
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



@login_required
def update_job(request,pk):
    data = JobPost.objects.get(pk=pk)
    form = JobPostForm(instance = data)
    if request.method == "POST": 
        form = JobPostForm(request.POST,instance = data)
        if form.is_valid():
            form.save()
            return redirect('listed-job')
    else: 
        context = {
            'form':form
        }

    return render(request,'administrator/update_job.html',context)



@login_required
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

@login_required
def delete_qualification(request,pk):
    data = Qualification.objects.get(pk=pk)
    data.delete()
    return redirect('qualification-dashboard')
    



@login_required
def delete_job(request,pk):
    data = JobPost.objects.get(pk=pk)
    data.delete()
    return redirect('listed-job')
    




@login_required
def delete_position(request,pk):
    data = Position.objects.get(pk=pk)
    data.delete()
    return redirect('position-dashboard')


@login_required
def position_dashboard(request): 
    positions = Position.objects.all()
    context = {
        "positions":positions
    }

    return render(request, 'administrator/position.html',context)


@login_required
def create_job(request):
    form = JobPostForm()

    if request.method == 'POST':
        form = JobPostForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('qualification-dashboard')

    context = {
            'form':form
        }
    
    return render(request,'administrator/create_job.html',context)


@login_required
def listing_jobs(request):
    listed_jobs = JobPost.objects.all()


    print(listed_jobs[0].id)
    context = {
        'listed_jobs' : listed_jobs
    }

    return render(request,"administrator/list_jobs.html",context)



def login_user(request):
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("admin_index")
    

    return render(request,'administrator/login.html')



# def login_user(request):

#     username = password = ''
#     if request.POST:
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(username=username, password=password)
#         if user is not None:
         
#             login(request, user)
#             return redirect("admin_index")
    

#     return render(request,'administrator/login.html')



def ServicesUpdate(request,id):
    service = Service.objects.get(id=id)
    points = service.points.all()

    context = {
        "points":points,
        "service":service
    }

    return render(request,'administrator/position.html',context)


