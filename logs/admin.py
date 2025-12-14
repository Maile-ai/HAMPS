from django.contrib import admin
from .models import ActivityLog


@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ("owner", "action", "device", "rule", "created_at")
    list_filter = ("action", "created_at")
    search_fields = ("owner__username", "description")
