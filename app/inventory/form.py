from django import forms
from .models import DeviceType, DeviceModel, Device

class DeviceForm(forms.ModelForm):

    class Meta:
        model = Device
        fields = (
            'deviceModel',
            'deviceType',
            'site',
            'ownership',
            'serialnumber',
            'deviceOwner'
            'submittor',
            'remarks',
        )

        widget = {
            'deviceModel': form.Select(attr={'placeholder'})
        }