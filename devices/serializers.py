from rest_framework import serializers
from .models import Device


class DeviceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Device
        fields = "__all__"
