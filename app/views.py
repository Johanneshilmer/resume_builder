from django.shortcuts import render, redirect
from .models import Resume, Education, Experience, Skill
from .forms import ResumeForm, EducationForm, ExperienceForm, SkillForm

def create_resume(request):
  if request.method == "POST":
    form1 = ResumeForm(request.POST, request.FILES)
    form2 = EducationForm(request.POST)
    form3 = ExperienceForm(request.POST)
    form4 = SkillForm(request.POST)
    
    # Get the data of chosen Template.
    template = request.POST.get('get_template', '')
    
    if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
      resume_instance = form1.save()
      # Set the resume foreign key for the Education form
      form2.instance.resume = resume_instance
      form2.save()
      form3.instance.resume = resume_instance
      form3.save()
      form4.instance.resume = resume_instance
      form4.save()
      
      print("det funkar")
      return redirect(template, pk=form1.instance.id)
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

def resume(request, pk):
  data1 = Resume.objects.filter(id=pk)
  data2 = Education.objects.filter(resume_id=pk)
  data3 = Experience.objects.filter(resume_id=pk)
  data4 = Skill.objects.filter(resume_id=pk)
  
  context = {
    "data1":data1,
    "data2":data2,
    "data3":data3,
    "data4":data4
  }
  return render(request,"resume.html", context=context)
