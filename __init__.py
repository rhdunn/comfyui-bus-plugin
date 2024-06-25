# Copyright (C) 2024 Reece H. Dunn. SPDX-License-Identifier: GPL-3

from .checkpoint_bus_node import CheckpointBusNode
from .latent_image_bus_node import LatentImageBusNode
from .parameters_bus_node import ImageSizeBusNode, ImageParameterBusNode, LatentImageParameterBusNode
from .prompt_bus_node import PromptBusNode, PromptSDXLBusNode, CLIPEncodedPromptBusNode

NODE_CLASS_MAPPINGS = {
    "ComfyBus.CheckpointBusNode": CheckpointBusNode,
    "ComfyBus.CLIPEncodedPromptBusNode": CLIPEncodedPromptBusNode,
    "ComfyBus.ImageParameterBusNode": ImageParameterBusNode,
    "ComfyBus.ImageSizeBusNode": ImageSizeBusNode,
    "ComfyBus.LatentImageBusNode": LatentImageBusNode,
    "ComfyBus.LatentImageParameterBusNode": LatentImageParameterBusNode,
    "ComfyBus.PromptBusNode": PromptBusNode,
    "ComfyBus.PromptSDXLBusNode": PromptSDXLBusNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyBus.CheckpointBusNode": "Checkpoint Bus",
    "ComfyBus.CLIPEncodedPromptBusNode": "CLIP Encoded Prompt Bus",
    "ComfyBus.ImageParameterBusNode": "Image Parameter Bus",
    "ComfyBus.ImageSizeBusNode": "Image Size Bus",
    "ComfyBus.LatentImageBusNode": "Latent Image Bus",
    "ComfyBus.LatentImageParameterBusNode": "Latent Image Parameter Bus",
    "ComfyBus.PromptBusNode": "Prompt Bus",
    "ComfyBus.PromptSDXLBusNode": "Prompt SDXL Bus"
}
