from datetime import datetime
from .models import Rule


def is_device_blocked(device):
    """
    Returns True if the device should be blocked
    based on active rules and current time.
    """
    now = datetime.now().time()

    rules = Rule.objects.filter(
        device=device,
        is_active=True
    )

    for rule in rules:
        if rule.start_time <= now <= rule.end_time:
            if rule.action == "BLOCK":
                return True

    return False
