from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView

class HomeView(TemplateView):
    template_name = "website/home.html"
