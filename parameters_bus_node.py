# Copyright (C) 2024 Reece H. Dunn. SPDX-License-Identifier: GPL-3


MAX_RESOLUTION=16384


# noinspection PyPep8Naming,PyMethodMayBeStatic,PyRedundantParentheses,PyMethodParameters
class ImageSizeBusNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"width": ("INT", {"default": 1024, "min": 256, "max": MAX_RESOLUTION, "step": 8, "defaultInput": True}),
                             "height": ("INT", {"default": 1024, "min": 256, "max": MAX_RESOLUTION, "step": 8, "defaultInput": True})}
                }

    RETURN_TYPES = ("INT", "INT", )
    RETURN_NAMES = ("width", "height", )

    FUNCTION = "bus"
    CATEGORY = "ComfyBus"

    def bus(self, width, height):
        return (width, height)
