from django.forms import ModelForm 
from .models import JobSeeker,Vacancy


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


class VacancyForm(ModelForm):


    class Meta:
        model = Vacancy
        fields = [
            'job_title',
            'proposed_commencement_Date',
            'attachment_position_description',
            'name',
            'email',
            'contact',
            'additional_info',
                    ]