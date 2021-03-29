from django import forms
from .models import DeviceType, DeviceModel, Device


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = (
            "deviceModel",
            "deviceType",
            "site",
            "ownership",
            "serialnumber",
            "deviceOwner",
            "submittor",
            "remarks",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["deviceModel"].queryset = DeviceModel.objects.none()

        if "deviceType" in self.data:
            try:
                deviceType_id = int(self.data.get("deviceType"))
                self.fields["deviceModel"].queryset = DeviceModel.objects.filter(
                    deviceType_id=deviceType_id
                ).order_by("name")
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty deviceModel queryset
        elif self.instance.pk:
            self.fields[
                "deviceModel"
            ].queryset = self.instance.deviceType.deviceModel_set.order_by("name")
