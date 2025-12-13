from django.contrib import admin
from .models import Device, RestrictionRule


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = (
        "hostname",
        "ip_address",
        "mac_address",
        "device_type",
        "connection_type",
        "group",
        "owner",
        "last_seen",
    )

    list_filter = (
        "group",
        "connection_type",
        "device_type",
    )

    search_fields = (
        "hostname",
        "ip_address",
        "mac_address",
        "owner__username",
    )

    readonly_fields = (
        "created_at",
        "last_seen",
    )

    ordering = ("-last_seen",)


@admin.register(RestrictionRule)
class RestrictionRuleAdmin(admin.ModelAdmin):
    list_display = (
        "group",
        "active",
        "block_internet",
        "schedule_start",
        "schedule_end",
        "created_at",
    )

    list_filter = (
        "active",
        "group",
    )

    readonly_fields = (
        "created_at",
    )

    ordering = ("group",)
