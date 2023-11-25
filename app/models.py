from django.db import models

class Resume(models.Model):
  name = models.CharField(max_length=255)
  phone = models.CharField(max_length=15)
  email = models.EmailField()
  image = models.ImageField(upload_to="uploads/")
  header = models.CharField(max_length=255)

class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    degree = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    graduation_year = models.IntegerField()

class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

class Skill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    proficiency = models.CharField(max_length=50)
