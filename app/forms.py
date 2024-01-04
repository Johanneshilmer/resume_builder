from django import forms
from .models import *
from django.forms import TextInput, ClearableFileInput

class ResumeForm(forms.ModelForm):
  class Meta:
    model = Resume
    fields = "__all__"
    

class EducationForm(forms.ModelForm):
  class Meta:
    model = Education
    fields = ["school", "degree", "graduation_year"]
    
    
class ExperienceForm(forms.ModelForm):
  class Meta:
    model = Experience
    fields = ["company", "description", "start_date", "end_date"]


class SkillForm(forms.ModelForm):
  class Meta:
    model = Skill
    fields = ["skills"]