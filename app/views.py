from django.shortcuts import render
from .models import Resume, Education, Experience, Skill
from .forms import ResumeForm, EducationForm, ExperienceForm, SkillForm

def create_resume(request):

  if request.method == "POST":
    form1 = ResumeForm(request.POST, request.FILES)
    form2 = EducationForm(request.POST)
    form3 = ExperienceForm(request.POST)
    form4 = SkillForm(request.POST)
    if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
      form1.save()
      form2.save()
      form3.save()
      form4.save()
      return render(request, "resume.html")
  else:
    form1 = ResumeForm()
    form2 = EducationForm()
    form3 = ExperienceForm()
    form4 = SkillForm()
  
  context = {
    "form1":form1,
    "form2":form2,
    "form3":form3,
    "form4":form4,
  }
  return render(request, "home.html", context=context)

def resume(request):
  data = Resume.objects.all()
  return render(request,"resume.html", {"data":data})
