from django.forms import ModelForm 
from website.models import Qualification,Position


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