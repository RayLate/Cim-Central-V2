from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from django.urls import reverse_lazy
from .models import Device

# Create your views here.


class HomePageView(TemplateView):
    template_name = "index.html"


class DeviceListView(ListView):
    model = Device
    template_name = "inventory.html"


class DeviceCreateView(CreateView):
    model = Device
    template_name = "deploy.html"
    success_url = reverse_lazy('inventory_main')
