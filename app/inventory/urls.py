from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('inventory/', views.DeviceListView.as_view(), name='inventory_main'),
    path('deploy/', views.DeviceCreateView.as_view(), name='device_deploy'),
    path('deployed/<int:pk>/', views.DeployedDetailView.as_view(), name='deployed_success'),
]
