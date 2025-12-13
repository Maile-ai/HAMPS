from django.contrib import admin
from .models import Device, RestrictionRule, AccessLog

admin.site.register(Device)
admin.site.register(RestrictionRule)
admin.site.register(AccessLog)
