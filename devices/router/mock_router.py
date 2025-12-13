"""
Mock router interface for HAMPS
Simulates router behavior for device discovery and access control
"""

import random
from datetime import timedelta

MOCK_DEVICES = [
    {
        "hostname": "kids-tablet",
        "ip_address": "192.168.0.12",
        "mac_address": "AA:BB:CC:DD:EE:01",
        "device_type": "Tablet",
        "connection_type": "wifi",
        "lease_remaining": 120,
    },
    {
        "hostname": "dad-laptop",
        "ip_address": "192.168.0.15",
        "mac_address": "AA:BB:CC:DD:EE:02",
        "device_type": "Laptop",
        "connection_type": "wifi",
        "lease_remaining": 300,
    },
    {
        "hostname": "smart-tv",
        "ip_address": "192.168.0.20",
        "mac_address": "AA:BB:CC:DD:EE:03",
        "device_type": "TV",
        "connection_type": "ethernet",
        "lease_remaining": 500,
    },
]


def fetch_connected_devices():
    """
    Simulate fetching connected devices from a router
    """
    devices = []

    for device in MOCK_DEVICES:
        device_copy = device.copy()
        device_copy["lease_remaining"] = max(
            0, device["lease_remaining"] - random.randint(1, 10)
        )
        devices.append(device_copy)

    return devices


def block_device(mac_address):
    """
    Simulate blocking a device
    """
    return {
        "status": "blocked",
        "mac_address": mac_address
    }


def unblock_device(mac_address):
    """
    Simulate unblocking a device
    """
    return {
        "status": "unblocked",
        "mac_address": mac_address
    }
