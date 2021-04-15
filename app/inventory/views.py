from django.db.models import Q
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)
from django.views.generic.base import ContextMixin

from .form import DeviceForm
from .models import Device, DeviceModel

# Render View


def load_models(request):
    deviceType_id = request.GET.get("type")
    models = DeviceModel.objects.filter(deviceType_id=deviceType_id).order_by("name")
    return render(request, "model_dropdown_list_options.html", {"models": models})


def check_unique_serial_number(request):
    serial_number = request.GET.get("serialnumber")
    # print(serial_number)
    exist = Device.objects.filter(serialnumber=serial_number).exists()
    if not exist:
        return HttpResponse(f"{serial_number} is unique")
    else:
        return HttpResponseBadRequest()


# Create your views here.


class HomePageView(TemplateView):
    template_name = "index.html"


class DeployedSearchView(TemplateView):
    template_name = "deployed_search.html"


class ReturnSearchView(TemplateView):
    template_name = "return_search.html"


class DeviceListView(ListView):
    model = Device
    template_name = "inventory.html"


class DeviceCreateView(CreateView):
    model = Device
    form_class = DeviceForm
    template_name = "deploy_single.html"


class BulkDeviceCreateView(DeviceCreateView):
    template_name = "deploy_bulk.html"


class DeployedDetailView(DetailView):
    model = Device
    template_name = "device_detail.html"


class DeviceUpdateView(UpdateView):
    model = Device
    template_name = "device_update.html"
    fields = "__all__"


class DeviceSearchView(ListView):
    model = Device
    template_name = "device_search_result.html"

    def get_queryset(self):  # new
        serialnum = self.request.GET.get("serialnum")
        userid = self.request.GET.get("userid")
        if serialnum:
            object_list = Device.objects.filter(Q(serialnumber__icontains=serialnum))

        if userid:
            object_list = Device.objects.filter(Q(deviceOwner__icontains=userid))
            # print(len(object_list))
        return object_list


class ReturnDeviceSearchView(DeviceSearchView):
    model = Device
    template_name = "return_search_result.html"

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            device_ids = request.POST.get("ids", "")
            device_ids = device_ids.split(",")
            print(device_ids)
            self.model.objects.filter(id__in=device_ids).delete()
            return JsonResponse({"status": "ok"}, status=204)
