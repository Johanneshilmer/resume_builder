from django import forms
from .models import *
from django.forms import TextInput,  EmailInput

class ResumeForm(forms.ModelForm):
  class Meta:
    model = Resume
    fields = "__all__"
    # Styling for the forms
    widgets = {
      "name": TextInput(attrs={
        'style': 'max-width: 300px; width: 300px;', # Adding flera styles
        'placeholder': 'Name'
      }),
      "email": EmailInput(attrs={
        #'class': "form-control", Detta är bootstrap för att få i paragraf.
        'style': "max-width: 300px",
        'placeholder': "Email"
      })
    }

class EducationForm(forms.ModelForm):
  class Meta:
    model = Education
    fields = ["degree", "school", "graduation_year"]
    
class ExperienceForm(forms.ModelForm):
  class Meta:
    model = Experience
    fields = ["title", "company", "start_date", "end_date"]

class SkillForm(forms.ModelForm):
  class Meta:
    model = Skill
    fields = ["name", "proficiency"]