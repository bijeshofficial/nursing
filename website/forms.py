from django.forms import ModelForm 
from .models import JobSeeker


class JobSeekerForm(ModelForm):
    class Meta:
        model = JobSeeker
        fields = ['qualification_id',
                        'position_id',
                        'first_name',
                        'last_name',
                        'phone_number',
                        'email',
                        'work_experience',
                        'current_police_check',
                        'children_check',
                        'address',
                        'cv',
                        'qualification_pdf']