# Copyright (C) 2024 Reece H. Dunn. SPDX-License-Identifier: GPL-3


# noinspection PyPep8Naming,PyMethodMayBeStatic,PyRedundantParentheses,PyMethodParameters
class PromptBusNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"positive": ("STRING", {"default": "", "multiline": True, "defaultInput": True}),
                             "negative": ("STRING", {"default": "", "multiline": True, "defaultInput": True})}
                }

    RETURN_TYPES = ("STRING", "STRING", )
    RETURN_NAMES = ("positive", "negative", )

    FUNCTION = "bus"
    CATEGORY = "ComfyBus"

    def bus(self, positive, negative):
        return (positive, negative)
