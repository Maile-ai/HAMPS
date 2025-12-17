from django.urls import path
from .views import (
    DeviceListView,
    DeviceDetailView,
    AssignDeviceGroupView,
    RouterRefreshView,
    CreateRuleView,
    UpdateRuleView,
    ActiveRulesView,
    ApplyRestrictionRuleView,  
)

urlpatterns = [
    # Devices
    path("", DeviceListView.as_view(), name="device-list"),
    path("<int:pk>/", DeviceDetailView.as_view(), name="device-detail"),
    path("group/assign/", AssignDeviceGroupView.as_view(), name="assign-device-group"),

    # Router
    path("router/refresh/", RouterRefreshView.as_view(), name="router-refresh"),

    # Rules
    path("rules/create/", CreateRuleView.as_view(), name="rule-create"),
    path("rules/<int:pk>/update/", UpdateRuleView.as_view(), name="rule-update"),
    path("rules/active/", ActiveRulesView.as_view(), name="active-rules"),
    path("rules/apply/", ApplyRestrictionRuleView.as_view(), name="apply-rule"),  
]
