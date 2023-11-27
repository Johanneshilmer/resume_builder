from django.urls import path
from .views import create_resume, resume, index,test

urlpatterns = [
    path('', index),
    path('form/', create_resume, name="form"),
    path('resume/<int:pk>/', resume, name="resume"),
    path('test/', test)
]
