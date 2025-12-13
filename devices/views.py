from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Device
from .serializers import DeviceSerializer


class DeviceListView(generics.ListAPIView):
    """
    GET /api/devices/
    List all devices belonging to the logged-in user
    """
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Device.objects.filter(owner=self.request.user)


class DeviceDetailView(generics.RetrieveAPIView):
    """
    GET /api/devices/<id>/
    Retrieve a single device
    """
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Device.objects.filter(owner=self.request.user)


class AssignDeviceGroupView(APIView):
    """
    POST /api/devices/group/assign/
    Assign a device to a group
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
            device = Device.objects.get(
                id=device_id,
                owner=request.user
            )
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
