from . import views
from django.urls import include, path

urlpatterns = [
    # Edit Single Entry
    path('deploy/<int:pk>/edit/', views.DeviceUpdateView.as_view(), name='device_update'),

    # Search Result
    path('search/deployed/result/', views.DeviceSearchView.as_view(), name='device_search_result'),
    path('search/return/result/', views.ReturnDeviceSearchView.as_view(), name='return_search_result'),

    path('search/deployed/', views.DeployedSearchView.as_view(), name='deploy_search'),
    path('search/return/', views.ReturnSearchView.as_view(), name='return_search'),
    path('inventory/', views.DeviceListView.as_view(), name='inventory_main'),
    path('deploy/', views.DeviceCreateView.as_view(), name='device_deploy'),
    path('deploy/<int:pk>/', views.DeployedDetailView.as_view(), name='device_detail'),
    path('', views.HomePageView.as_view(), name='home'),
]
