# Copyright (C) 2024 Reece H. Dunn. SPDX-License-Identifier: GPL-3

from .checkpoint_bus_node import CheckpointBusNode
from .clip_bus_node import CLIPConditioningBusNode
from .image_bus_node import LatentImageBusNode, ImageBusNode
from .parameters_bus_node import (
    ImageSizeBusNode,
    ImageParameterBusNode,
    LatentImageParameterBusNode,
    ImageScaleToSideParameterBusNode
)
from .prompt_bus_node import PromptBusNode, PromptSDXLBusNode, CLIPEncodedPromptBusNode

NODE_CLASS_MAPPINGS = {
    "ComfyBus.CheckpointBusNode": CheckpointBusNode,
    "ComfyBus.CLIPConditioningBusNode": CLIPConditioningBusNode,
    "ComfyBus.CLIPEncodedPromptBusNode": CLIPEncodedPromptBusNode,
    "ComfyBus.ImageBusNode": ImageBusNode,
    "ComfyBus.ImageParameterBusNode": ImageParameterBusNode,
    "ComfyBus.ImageScaleToSideParameterBusNode": ImageScaleToSideParameterBusNode,
    "ComfyBus.ImageSizeBusNode": ImageSizeBusNode,
    "ComfyBus.LatentImageBusNode": LatentImageBusNode,
    "ComfyBus.LatentImageParameterBusNode": LatentImageParameterBusNode,
    "ComfyBus.PromptBusNode": PromptBusNode,
    "ComfyBus.PromptSDXLBusNode": PromptSDXLBusNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyBus.CheckpointBusNode": "Checkpoint Bus",
    "ComfyBus.CLIPConditioningBusNode": "CLIP Conditioning Bus",
    "ComfyBus.CLIPEncodedPromptBusNode": "CLIP Encoded Prompt Bus",
    "ComfyBus.ImageBusNode": "Image Bus",
    "ComfyBus.ImageParameterBusNode": "Image Parameter Bus",
    "ComfyBus.ImageScaleToSideParameterBusNode": "Image Scale to Side Parameter Bus",
    "ComfyBus.ImageSizeBusNode": "Image Size Bus",
    "ComfyBus.LatentImageBusNode": "Latent Image Bus",
    "ComfyBus.LatentImageParameterBusNode": "Latent Image Parameter Bus",
    "ComfyBus.PromptBusNode": "Prompt Bus",
    "ComfyBus.PromptSDXLBusNode": "Prompt SDXL Bus"
}
