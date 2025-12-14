from django.conf import settings
from django.db import models
from devices.models import Device


class Rule(models.Model):
    """
    Defines time-based access rules for a device.
    """

    ACTION_CHOICES = [
        ("ALLOW", "Allow"),
        ("BLOCK", "Block"),
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="rules"
    )

    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
        related_name="rules"
    )

    start_time = models.TimeField(
        help_text="Time when the rule starts"
    )

    end_time = models.TimeField(
        help_text="Time when the rule ends"
    )

    action = models.CharField(
        max_length=10,
        choices=ACTION_CHOICES
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"{self.device.name} | "
            f"{self.action} | "
            f"{self.start_time} - {self.end_time}"
        )
