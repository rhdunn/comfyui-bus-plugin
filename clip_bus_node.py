# Copyright (C) 2024 Reece H. Dunn. SPDX-License-Identifier: GPL-3


# noinspection PyPep8Naming,PyMethodMayBeStatic,PyRedundantParentheses,PyMethodParameters
class CLIPConditioningBusNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {},
                "optional": {"clip_vision": ("CLIP_VISION_OUTPUT", ),
                             "strength": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.01, "defaultInput": True}),
                             "noise_augmentation": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.01, "defaultInput": True})}
                }

    RETURN_TYPES = ("CLIP_VISION_OUTPUT", "FLOAT", "FLOAT", )
    RETURN_NAMES = ("clip_vision", "strength", "noise_augmentation", )

    FUNCTION = "bus"
    CATEGORY = "ComfyBus"

    def bus(self, clip_vision=None, strength=1.0, noise_augmentation=0.0):
        return (clip_vision, strength, noise_augmentation)
