# Ecosphere Card Generator (using Stable Diffusion)

A Python program that uses Stable Diffusion to generate Ecosphere card art (and then writes the card stats, just to be
complete). AKA `Ecosphere | SD | PIL`.

## Usage

Run the program with one of the following commands, executed from within the activated virtual environment in the base
directory containing the `README.md`.

- `python card-maker/make_stats.py`: Only write card stats. Outputs to `output/finished_cards/stats/`.
- `python card-maker/make_art.py`: Only write card art. Outputs to `output/finished_cards/art/`.
- `python card-maker/make_both.py`: Write card stats and art. Outputs to `output/finished_cards/art_and_stats/`.

### Card Stats

Card stats are read from the CSV file `assets_data/card_database.csv`. This file is the exact same as Neo's official
Card Database Google Sheets document, except I've added an Art Description column after Text. This column contains part
of the prompt used in image generation (additional prompt is added in the program). This column is incomplete, only
having data for 12 cards.

### Image Generation

Raw artwork is saved to `output/generated_artwork/`.

The seed for image generation is hardcoded to `27`. This means that, when the program is run twice, and an image prompt
is not changed, it will generate the exact same image. To change this, you can edit line 20 of `card_maker/make_art.py`

See the above Card Stats section for information on image generation prompts.

## Installation

### Virtual Environment

You'll need to setup a `venv` for this, because there are so many specific dependencies.

1. Install `virtualenv` globally with `pip install virtualenv`
2. Create a `venv` in your cwd with `virtualenv --python C:/Python/Python310/python.exe venv` (replacing with your
   absolute Python executable path)
3. Enter the `venv` with `.\venv\Scripts\activate`. Now, all commands run from the terminal will affect the virtual
   environment and will be isolated from the larger system

All commands (including below installation commands) should be executed from within the activated virtual environment.

### Python Requirements

Install dependencies with `pip install -r requirements.txt`.

### opencv-python

1. Download opencv-python wheel
   file [here](https://files.pythonhosted.org/packages/70/98/b7143877dc53467deea6ba74f9161794db5f23698a6dbded5a9718f89d9c/opencv_python-4.1.2.30-cp38-cp38-win_amd64.whl)
2. Rename file to `opencv_python-4.1.2.30-cp38-abi3-win_amd64.whl`.
3. Install with `pip install opencv_python-4.1.2.30-cp38-abi3-win_amd64.whl`

### CUDA/Torch

1. Download CUDA installer
   from [here](https://developer.nvidia.com/cuda-11-7-0-download-archive?target_os=Windows&target_arch=x86_64&target_version=11&target_type=exe_local)
2. Install CUDA from installer
3. Uninstall the wrong packages that were installed a few steps ago (sorry :/)
   with `pip uninstall torch torchvision torchaudio` (you'll need to enter "y" to confirm it)
3. Install torch packages
   with `pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117`)

### Stable Diffusion Model

Place `model.ckpt` at location: `stable-diffusion-main/models/ldm/stable-diffusion-v1/model.ckpt`

(If you need a model, download Stable Diffusion 1.4
from [here](https://huggingface.co/CompVis/stable-diffusion-v-1-4-original/resolve/main/sd-v1-4.ckpt))

## License

I license all possible parts of this repository under GPLv3.

This is built off of the [Optimized Stable Diffusion fork](https://github.com/basujindal/stable-diffusion/), which was
forked while SD was licensed under an All Rights Reserved license (before it was changed to the CreativeML Open RAIL M
License). I'm not sure what the legal implications are for licensing this, but note that parts of this might be licensed
under that.