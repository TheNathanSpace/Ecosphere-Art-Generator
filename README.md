# Ecosphere Card Generator

A Python program that writes card stats to the blank card image.

## Usage

Run the program with `python card-maker/make_stats.py`, executed from within the activated virtual environment in the
base directory containing the `README.md`. This command will write card stats to `output/finished_cards/stats/`.

To clownify, run normally as above, then run `python card-maker/clownify.py`. Output will be
in `output/finished_cards/clown/`.

To only export specific rows, edit `rows_to_export.txt` in the following format:

```
25, 55, 18, 99, 145, 14848
```

Rows that don't exist will be ignored. If file is empty (no characters), it will export all rows.

### Card Stats

Card stats are read from the CSV file `assets_data/card_database.csv`. This file is the exact same as Neo's official
Card Database Google Sheets document, except I've added an Art Description column after Text. This column contains part
of the prompt used in image generation (additional prompt is added in the program). This column is incomplete, only
having data for 12 cards.

## Installation

Install dependencies with `pip install -r requirements.txt`. If you wish to separate this from your global Python
installation, see the below section on using a virtual environment. (Right now, literally the only requirement is
Pillow, so you could probably just install it globally)

### Virtual Environment

1. Install `virtualenv` globally with `pip install virtualenv`
2. Create a `venv` in your cwd with `virtualenv --python C:/Python/Python310/python.exe venv` (replacing with your
   absolute Python executable path)
3. Enter the `venv` with `.\venv\Scripts\activate`. Now, all commands run from the terminal will affect the virtual
   environment and will be isolated from the larger system

All commands (including installation commands) should be executed from within the activated virtual environment. You can
now install from `requirements.txt` (see above section).