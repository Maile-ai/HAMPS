from django.conf import settings
from django.db import models
from devices.models import Device
from rules.models import Rule


class ActivityLog(models.Model):
    ACTION_CHOICES = (
        ("BLOCK", "Blocked"),
        ("UNBLOCK", "Unblocked"),
        ("RULE_CREATED", "Rule Created"),
        ("RULE_UPDATED", "Rule Updated"),
        ("MANUAL_OVERRIDE", "Manual Override"),
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="activity_logs"
    )
    device = models.ForeignKey(
        Device,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    rule = models.ForeignKey(
        Rule,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.owner} | {self.action} | {self.created_at}"