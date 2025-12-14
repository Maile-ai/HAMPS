from django.urls import path
from .views import (
    DeviceListView,
    DeviceDetailView,
    AssignDeviceGroupView,
    RouterRefreshView,
    CreateRuleView,
    UpdateRuleView,
    ActiveRulesView,
)

urlpatterns = [
    # Devices
    path("", DeviceListView.as_view(), name="device-list"),
    path("<int:pk>/", DeviceDetailView.as_view(), name="device-detail"),
    path("group/assign/", AssignDeviceGroupView.as_view()),

    # Router
    path("router/refresh/", RouterRefreshView.as_view()),

    # Rules
    path("rules/create/", CreateRuleView.as_view()),
    path("rules/<int:pk>/update/", UpdateRuleView.as_view()),
    path("rules/active/", ActiveRulesView.as_view()),
]
