from django.shortcuts import render, redirect
from .models import Resume, Education, Experience, Skill
from .forms import ResumeForm, EducationForm, ExperienceForm, SkillForm
from django.forms import inlineformset_factory

def index(request):
  return render(request,"index.html")


def create_resume(request):
  if request.method == "POST":
    form1 = ResumeForm(request.POST, request.FILES)
    form2 = EducationForm(request.POST)
    form3 = ExperienceForm(request.POST)
    form4 = SkillForm(request.POST)
    
    EducationFormSet = inlineformset_factory(Resume, Education, form=EducationForm, extra=1)
    SkillFormSet = inlineformset_factory(Resume, Skill, form=SkillForm, extra=1)
    
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
      
      # Process formsets for Education and Skills
      education_formset = EducationFormSet(request.POST, instance=resume_instance)
      skill_formset = SkillFormSet(request.POST, instance=resume_instance)
      if education_formset.is_valid():
                education_formset.save()

      if skill_formset.is_valid():
          skill_formset.save()
      
      # Store the template in the session
      request.session['chosen_template'] = template
      
      return redirect("resume", pk=form1.instance.id)
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
  return render(request, "form.html", context=context)


def resume(request, pk):
  # Retrieve the chosen template from the session
  chosen_template = request.session.get('chosen_template', '')
  
  data1 = Resume.objects.filter(id=pk)
  data2 = Education.objects.filter(resume_id=pk)
  data3 = Experience.objects.filter(resume_id=pk)
  data4 = Skill.objects.filter(resume_id=pk)
  
  context = {
    "data1":data1,
    "data2":data2,
    "data3":data3,
    "data4":data4,
  }
  return render(request, chosen_template, context=context)