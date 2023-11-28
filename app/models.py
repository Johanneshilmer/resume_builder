from django.db import models

class Resume(models.Model):
  name = models.CharField(max_length=255)
  phone = models.CharField(max_length=15)
  email = models.EmailField()
  image = models.ImageField(upload_to="uploads/", blank=True, null=True)
  title = models.CharField(max_length=255)
  
  def __str__(self):
      return self.name

class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    school = models.CharField(max_length=255)
    degree = models.CharField(max_length=255, blank=True, null=True)
    graduation_year = models.DateField(blank=True, null=True)

class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

class Skill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    skills = models.CharField(max_length=255)
