from django import forms
from .models import *

class ResumeForm(forms.ModelForm):
  class Meta:
      model = Resume
      fields = "__all__"

class EducationForm(forms.ModelForm):
  class Meta:
    model = Education
    fields = ["degree", "school", "graduation_year"]
    
class ExperienceForm(forms.ModelForm):
  class Meta:
    models = Experience
    fields = ["title", "company", "start_date", "end_date"]

class SkillForm(forms.ModelForm):
  class Meta:
    models = Skill
    fields = ["name", "proficiency"]