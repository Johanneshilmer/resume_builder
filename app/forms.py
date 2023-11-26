from django import forms
from .models import *
from django.forms import TextInput

class ResumeForm(forms.ModelForm):
  class Meta:
    model = Resume
    fields = "__all__"
    # Styling for the forms
    widgets = {
      "name": TextInput(attrs={
        'class': "form-control",
        'style': 'max-width: 300px',
        'placeholder': 'Name'
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