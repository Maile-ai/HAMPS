from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Device, RestrictionRule
from .serializers import DeviceSerializer, RestrictionRuleSerializer


# =========================
# DEVICES
# =========================

class DeviceListView(generics.ListCreateAPIView):
    """
    GET  /api/devices/   → list user's devices
    POST /api/devices/   → create a new device
    """
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Device.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DeviceDetailView(generics.RetrieveAPIView):
    """
    GET /api/devices/<id>/
    """
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Device.objects.filter(owner=self.request.user)


class AssignDeviceGroupView(APIView):
    """
    POST /api/devices/group/assign/
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        device_id = request.data.get("device_id")
        group = request.data.get("group")

        if not device_id or not group:
            return Response(
                {"error": "device_id and group are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            device = Device.objects.get(id=device_id, owner=request.user)
        except Device.DoesNotExist:
            return Response(
                {"error": "Device not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        device.group = group
        device.save()

        return Response(
            {"message": f"Device assigned to {group}"},
            status=status.HTTP_200_OK
        )


# =========================
# ROUTER (MOCKED)
# =========================

class RouterRefreshView(APIView):
    """
    POST /api/router/refresh/
    Fetch devices from router (mocked)
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        return Response(
            {"message": "Router device list refreshed"},
            status=status.HTTP_200_OK
        )


# =========================
# RULES
# =========================

class CreateRuleView(generics.CreateAPIView):
    """
    POST /api/rules/create/
    """
    serializer_class = RestrictionRuleSerializer
    permission_classes = [permissions.IsAuthenticated]


class UpdateRuleView(generics.UpdateAPIView):
    """
    PUT /api/rules/<id>/update/
    """
    serializer_class = RestrictionRuleSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = RestrictionRule.objects.all()


class ActiveRulesView(generics.ListAPIView):
    """
    GET /api/rules/active/
    """
    serializer_class = RestrictionRuleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return RestrictionRule.objects.filter(active=True)
