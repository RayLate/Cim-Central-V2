from django.urls import include, path

from . import views

urlpatterns = [
    path('deploy/<int:pk>/edit/', views.DeviceUpdateView.as_view(), name='device_update'),
    path('search/result/', views.DeviceSearchView.as_view(), name='device_search_result'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('inventory/', views.DeviceListView.as_view(), name='inventory_main'),
    path('deploy/', views.DeviceCreateView.as_view(), name='device_deploy'),
    path('deploy/<int:pk>/', views.DeployedDetailView.as_view(), name='device_detail'),
    path('', views.HomePageView.as_view(), name='home'),
]
