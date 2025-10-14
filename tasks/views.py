from django.shortcuts import render
from django.views.generic import ListView
from .models import Task  # Using Task instead of Organization

class HomePageView(ListView):
    model = Task  # Changed from Organization to Task
    context_object_name = 'home'  # Keeping same as PDF
    template_name = "home.html"