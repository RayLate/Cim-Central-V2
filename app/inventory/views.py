from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DetailView
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
    fields = '__all__'
    success_url = reverse_lazy('deployed_success')

class DeployedDetailView(DetailView):
    model = Device
    template_name = "success_deployment.html"
