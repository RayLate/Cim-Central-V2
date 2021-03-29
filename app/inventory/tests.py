from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Device

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


class InventoryListViewTests(TestCase):
    def test_device_list_view(self):
        res = self.client.get(reverse("inventory_main"))
        self.assertEqual(200, res.status_code)
        self.assertTemplateUsed(res, "inventory.html")
