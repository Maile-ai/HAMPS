from rest_framework import serializers
from .models import Device, RestrictionRule


class DeviceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Device
        fields = "__all__"


class RestrictionRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestrictionRule
        fields = "__all__"
