from django.forms import ModelForm 
from website.models import Qualification,Position,JobPost
from django import forms
from ckeditor.widgets import CKEditorWidget



class QualificationForm(ModelForm):
    class Meta:
        model = Qualification
        fields = [
            'name'
        ]


class PositionForm(ModelForm):


    class Meta:
        model = Position
        fields = [
            'name'
                    ]



class JobPostForm(ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = JobPost
        fields = '__all__'
