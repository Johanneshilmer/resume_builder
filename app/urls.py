from django.urls import path
from .views import create_resume, resume

urlpatterns = [
    path('', create_resume),
    path('resume/', resume)
]
