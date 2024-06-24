# Copyright (C) 2024 Reece H. Dunn. SPDX-License-Identifier: GPL-3

from .latent_image_bus_node import LatentImageBusNode

NODE_CLASS_MAPPINGS = {
    "ComfyBus.LatentImageBusNode": LatentImageBusNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyBus.LatentImageBusNode": "Latent Image Bus"
}
