"""
Router client abstraction layer
HAMPS uses this instead of talking directly to the router
"""

from .mock_router import (
    fetch_connected_devices,
    block_device,
    unblock_device,
)


class RouterClient:
    def get_devices(self):
        return fetch_connected_devices()

    def block(self, mac_address):
        return block_device(mac_address)

    def unblock(self, mac_address):
        return unblock_device(mac_address)
