from django.urls import path
from .views import create_resume, resume, index

urlpatterns = [
    path('', index),
    path('form/', create_resume, name="form"),
    path('resume/<int:pk>/', resume, name="resume"),
]
