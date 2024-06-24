# Copyright (C) 2024 Reece H. Dunn. SPDX-License-Identifier: GPL-3

from .checkpoint_bus_node import CheckpointBusNode
from .latent_image_bus_node import LatentImageBusNode
from .prompt_bus_node import PromptBusNode, PromptSDXLBusNode

NODE_CLASS_MAPPINGS = {
    "ComfyBus.CheckpointBusNode": CheckpointBusNode,
    "ComfyBus.LatentImageBusNode": LatentImageBusNode,
    "ComfyBus.PromptBusNode": PromptBusNode,
    "ComfyBus.PromptSDXLBusNode": PromptSDXLBusNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyBus.CheckpointBusNode": "Checkpoint Bus",
    "ComfyBus.LatentImageBusNode": "Latent Image Bus",
    "ComfyBus.PromptBusNode": "Prompt Bus",
    "ComfyBus.PromptSDXLBusNode": "Prompt SDXL Bus"
}
