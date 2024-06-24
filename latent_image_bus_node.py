# Copyright (C) 2024 Reece H. Dunn. SPDX-License-Identifier: GPL-3


# noinspection PyPep8Naming,PyMethodMayBeStatic,PyRedundantParentheses,PyMethodParameters
class LatentImageBusNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"latent": ("LATENT", ),
                             "vae": ("VAE", )},
                }

    RETURN_TYPES = ("LATENT", "VAE", )
    RETURN_NAMES = ("latent", "vae", )

    FUNCTION = "bus"
    CATEGORY = "ComfyBus"

    def bus(self, latent, vae):
        return (latent, vae)
