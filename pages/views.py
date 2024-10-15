from django.shortcuts import render
from django.views.generic import TemplateView


class ContentView(TemplateView):
    template_name = 'layouts/base.html'

# Create your views here.
