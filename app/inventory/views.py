from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DetailView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Device

# Create your views here.


class HomePageView(TemplateView):
    template_name = "index.html"
    
class SearchView(TemplateView):
    template_name = "search.html"


class DeviceListView(ListView):
    model = Device
    template_name = "inventory.html"


class DeviceCreateView(CreateView):
    model = Device
    template_name = "deploy.html"
    fields = '__all__'

class DeployedDetailView(DetailView):
    model = Device
    template_name = "device_detail.html"
    
class DeviceUpdateView(UpdateView):
    model = Device
    template_name = "device_update.html"
    fields = '__all__'


class DeviceSearchView(ListView):
    model = Device
    template_name = "device_search_result.html"
    
    def get_queryset(self): # new
        serialnum = self.request.GET.get('serialnum')
        userid = self.request.GET.get('userid')
        if serialnum:
            object_list = Device.objects.filter(
            Q(serialnumber__icontains=serialnum)
            )
            return object_list
        if userid:
            object_list = Device.objects.filter(
            Q(deviceOwner__icontains=userid)
            )
            return object_list            
        
