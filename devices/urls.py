from django.urls import path
from .views import (
    DeviceListView,
    DeviceDetailView,
    AssignDeviceGroupView,
)

urlpatterns = [
    path("devices/", DeviceListView.as_view(), name="device-list"),
    path("devices/<int:pk>/", DeviceDetailView.as_view(), name="device-detail"),
    path("devices/group/assign/", AssignDeviceGroupView.as_view(), name="device-group-assign"),
]
