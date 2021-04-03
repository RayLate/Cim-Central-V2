from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from .models import Device, DeviceModel, DeviceType

hp840g6 = {
    "deviceType": "Laptop",
    "deviceModel": "HP 840 G6",
    "site": "F10N",
    "ownership": "Primary Device",
    "serialnumber": "test123",
    "deviceOwner": "rming",
}

hp840g5 = {
    "deviceType": "Laptop",
    "deviceModel": "HP 840 G5",
    "site": "F10N",
    "ownership": "Primary Device",
    "serialnumber": "test1233123",
    "deviceOwner": "rming",
}


# Create your tests here.
class InventoryTemplateViewTests(TestCase):
    def test_home_page_view_template(self):
        res = self.client.get(reverse("home"))
        self.assertEqual(200, res.status_code)
        self.assertTemplateUsed(res, "index.html")

    def test_deployed_search_view_template(self):
        res = self.client.get(reverse("deploy_search"))
        self.assertEqual(200, res.status_code)
        self.assertTemplateUsed(res, "deployed_search.html")

    def test_return_search_view_template(self):
        res = self.client.get(reverse("return_search"))
        self.assertEqual(200, res.status_code)
        self.assertTemplateUsed(res, "return_search.html")


class DeviceTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester123", email="test@test.com", password="test123"
        )

        type1 = DeviceType.objects.create(name="Laptop")

        model1 = DeviceModel.objects.create(
            name="HP 840 G6", deviceType=DeviceType.objects.get(pk=1)
        )
        model1 = DeviceModel.objects.create(
            name="HP 840 G5", deviceType=DeviceType.objects.get(pk=1)
        )

        self.device1 = Device.objects.create(
            deviceType=DeviceType.objects.get(pk=1),
            deviceModel=DeviceModel.objects.get(pk=1),
            site=hp840g6["site"],
            ownership=hp840g6["ownership"],
            serialnumber=hp840g6["serialnumber"],
            deviceOwner=hp840g6["deviceOwner"],
            submittor=User.objects.get(id=1),
        )

    def test_duplicate_serial_number(self):
        try:
            self.device2 = Device.objects.create(
                deviceType=DeviceType.objects.get(pk=1),
                deviceModel=DeviceModel.objects.get(pk=2),
                site=hp840g6["site"],
                ownership=hp840g6["ownership"],
                serialnumber=hp840g6["serialnumber"],
                deviceOwner=hp840g6["deviceOwner"],
                submittor=User.objects.get(id=1),
            )
        except IntegrityError as e:
            self.assertIn("UNIQUE", e.args[0])

    def test_device_entry(self):
        self.assertEqual(self.device1.pk, 1)
        self.assertEqual(str(self.device1.deviceType), "Laptop")
        self.assertEqual(str(self.device1.deviceModel), "HP 840 G6")
        self.assertEqual(str(self.device1.site), "F10N")
        self.assertEqual(str(self.device1.ownership), "Primary Device")
        self.assertEqual(str(self.device1.serialnumber), "test123".upper())
        self.assertEqual(str(self.device1.deviceOwner), "rming".upper())
        self.assertEqual(str(self.device1.submittor), "tester123")
        self.assertEqual(str(self.device1.remarks), "")

    def test_device_list_view(self):
        res = self.client.get(reverse("inventory_main"))
        self.assertEqual(200, res.status_code)
        self.assertTemplateUsed(res, "inventory.html")
        self.assertContains(res, "test123".upper())

    def test_device_detail_view(self):
        res = self.client.get("/deploy/1/")
        self.assertEqual(200, res.status_code)
        self.assertContains(res, "test123".upper())
        self.assertTemplateUsed(res, "device_detail.html")

        res = self.client.get("/deploy/100/")
        self.assertEqual(404, res.status_code)

    def test_device_create_view(self):
        res = self.client.post(
            reverse("device_deploy"),
            {
                "deviceType": DeviceType.objects.get(pk=1),
                "deviceModel": DeviceModel.objects.get(pk=1),
                "site": hp840g6["site"],
                "ownership": hp840g6["ownership"],
                "serialnumber": "second1",
                "deviceOwner": hp840g6["deviceOwner"],
                "submittor": User.objects.get(id=1),
                "remarks": "hello",
            },
        )
        self.assertEqual(302, res.status_code)
        self.assertTemplateUsed(res, "deploy_single.html")
        print(Device.objects.first().serialnumber)
        # self.assertContains(Device.objects.last().serialnumber, 'second1'.upper())
        # self.assertContains(Device.objects.last().deviceOwner, 'rming'.upper())
