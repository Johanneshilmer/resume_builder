from django.shortcuts import render
from .models import Resume, Education, Experience, Skill
from .forms import ResumeForm, EducationForm, ExperienceForm, SkillForm

def create_resume(request):
  if request.method == "POST":
    form = ResumeForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return render(request, "resume.html")
  else:
    form = ResumeForm()
  image = Resume.objects.all()
  return render(request, "home.html", {"form":form, "image":image})

def resume(request):
  data = Resume.objects.all()
  return render(request,"resume.html", {"data":data})
