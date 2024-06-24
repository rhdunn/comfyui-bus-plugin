# comfyui-bus-plugin
> A collection of nodes for rerouting multiple I/O lines together in a bus.

> [!NOTE]
>
> Because ComfyUI does not support generic I/O connections there have to be different
> nodes for the different combinations of data being passed around.

## Nodes
- Checkpoint Bus &ndash;
  Pass around the model, CLIP, and VAE from a loaded checkpoint.
- Latent Image Bus &ndash;
  Pass around a latent and VAE that can be passed to a VAE Decode node.
- Prompt Bus &ndash;
  Pass around the positive and negative prompt text strings.

## License
Copyright (C) 2024 Reece H. Dunn

SPDX-License-Identifier: [GPL-3](LICENSE)
