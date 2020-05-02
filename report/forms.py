from django.forms import ModelForm
from django import forms
from .models import Data


class DateInput(forms.DateInput):
    input_type = 'date'

class Form(ModelForm):
    class Meta:
        model = Data
        fields = ['name','reports', 'team_lead','hours', 'today_progress','today_doc', 'concern', 'next_plan', 'next_doc']
        widgets = {
               'team_lead': forms.RadioSelect()
              } 