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


# noinspection PyPep8Naming,PyMethodMayBeStatic,PyRedundantParentheses,PyMethodParameters
class PromptSDXLBusNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"positiveG": ("STRING", {"default": "", "multiline": True, "defaultInput": True}),
                             "positiveL": ("STRING", {"default": "", "multiline": True, "defaultInput": True}),
                             "negativeG": ("STRING", {"default": "", "multiline": True, "defaultInput": True}),
                             "negativeL": ("STRING", {"default": "", "multiline": True, "defaultInput": True})}
                }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", )
    RETURN_NAMES = ("positiveG", "positiveL", "negativeG", "negativeL", )

    FUNCTION = "bus"
    CATEGORY = "ComfyBus"

    def bus(self, positive_g, positive_l, negative_g, negative_l):
        return (positive_g, positive_l, negative_g, negative_l)


# noinspection PyPep8Naming,PyMethodMayBeStatic,PyRedundantParentheses,PyMethodParameters
class CLIPEncodedPromptBusNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"model": ("MODEL", ),
                             "positive": ("CONDITIONING", ),
                             "negative": ("CONDITIONING", )}
                }

    RETURN_TYPES = ("MODEL", "CONDITIONING", "CONDITIONING", )
    RETURN_NAMES = ("model", "positive", "negative", )

    FUNCTION = "bus"
    CATEGORY = "ComfyBus"

    def bus(self, model, positive, negative):
        return (model, positive, negative)
