# Change Log
> Release notes for comfyui-bus-plugin.

## [Unreleased]

### Added

The following nodes have been added:

| Name                        | Description                                                                       |
|-----------------------------|-----------------------------------------------------------------------------------|
| CLIP Conditioning Bus       | Parameters (all optional) for the unCLIPConditioning node.                        |

### Changed

### Removed

## [1.0.0] - 2024-06-26

### Added

The following nodes have been added:

| Name                        | Description                                                                       |
|-----------------------------|-----------------------------------------------------------------------------------|
| Checkpoint Bus              | Model, CLIP, and VAE from a loaded checkpoint.                                    |
| CLIP Encoded Prompt Bus     | CLIP Text Encoded positive and negative prompt and associated model.              |
| Image Bus                   | An image and mask from a loaded image, with optional VAE for VAE encoding.        |
| Image Parameter Bus         | Image width, height, and seed.                                                    |
| Image Size Bus              | Image width and height for the size of the image, target size, etc.               |
| Latent Image Bus            | A latent and VAE that can be passed to a VAE Decode node.                         |
| Latent Image Parameters Bus | A latent, seed, and denoise for an image2image KSampler source.                   |
| Prompt Bus                  | Positive and negative prompt text strings.                                        |
| Prompt SDXL Bus             | Positive and negative prompt text strings in the SDXL text_l and text_g variants. |

[Unreleased]: https://github.com/rhdunn/comfyui-bus-plugin/compare/1.0.0...HEAD
[1.0.0]: https://github.com/rhdunn/comfyui-bus-plugin/releases/tag/1.0.0
