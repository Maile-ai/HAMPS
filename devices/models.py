from django.db import models
from django.contrib.auth.models import User


class Device(models.Model):
    DEVICE_GROUP_CHOICES = [
        ("kids", "Kids"),
        ("teens", "Teens"),
        ("adults", "Adults"),
        ("guests", "Guests"),
    ]

    CONNECTION_TYPE_CHOICES = [
        ("wifi", "Wi-Fi"),
        ("ethernet", "Ethernet"),
    ]

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="devices"
    )

    hostname = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField(protocol="IPv4")
    mac_address = models.CharField(max_length=17)
    device_type = models.CharField(max_length=50)

    connection_type = models.CharField(
        max_length=10,
        choices=CONNECTION_TYPE_CHOICES,
        default="wifi"
    )

    lease_remaining = models.PositiveIntegerField(default=0)

    group = models.CharField(
        max_length=10,
        choices=DEVICE_GROUP_CHOICES,
        default="guests"
    )

    is_blocked = models.BooleanField(
        default=False,
        help_text="Whether internet access is currently blocked for this device"
    )

    last_seen = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.hostname} ({self.ip_address})"


class RestrictionRule(models.Model):
    GROUP_CHOICES = [
        ("kids", "Kids"),
        ("teens", "Teens"),
        ("adults", "Adults"),
        ("guests", "Guests"),
    ]

    group = models.CharField(
        max_length=10,
        choices=GROUP_CHOICES,
        unique=True
    )

    active = models.BooleanField(default=True)

    block_internet = models.BooleanField(
        default=False,
        help_text="Block internet access for this group"
    )

    schedule_start = models.TimeField(
        null=True,
        blank=True,
        help_text="Restriction start time"
    )

    schedule_end = models.TimeField(
        null=True,
        blank=True,
        help_text="Restriction end time"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rule for {self.group}"
