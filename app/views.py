from django.shortcuts import render
from .models import Resume, Education, Experience, Skill
from .forms import ResumeForm, EducationForm, ExperienceForm, SkillForm

def create_resume(request):
  if request.method == "POST":
    form1 = ResumeForm(request.POST, request.FILES)
    form2 = Education(request.POST, prefix="1-")
    if form1.is_valid() and form2.is_valid():
      form1.save()
      form2.save()
      return render(request, "resume.html")
  else:
    form1 = ResumeForm()
    form2 = Education()
  return render(request, "home.html", {"form1":form1,
                                       "form2":form2})

def resume(request):
  data = Resume.objects.all()
  return render(request,"resume.html", {"data":data})
