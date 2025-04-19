from django.urls import path
from . import views

urlpatterns = [
    path('', views.career_home, name= 'career_home'),
]