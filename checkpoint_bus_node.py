# Copyright (C) 2024 Reece H. Dunn. SPDX-License-Identifier: GPL-3


# noinspection PyPep8Naming,PyMethodMayBeStatic,PyRedundantParentheses,PyMethodParameters
class CheckpointBusNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"model": ("MODEL", ),
                             "clip": ("CLIP", ),
                             "vae": ("VAE", )},
                }

    RETURN_TYPES = ("MODEL", "CLIP", "VAE", )
    RETURN_NAMES = ("model", "clip", "vae", )

    FUNCTION = "bus"
    CATEGORY = "ComfyBus"

    def bus(self, model, clip, vae):
        return (model, clip, vae)
