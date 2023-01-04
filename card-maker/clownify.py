import json
from pathlib import Path

from PIL import Image

# Copy clown to card
if __name__ == '__main__':
    bounds_dict: dict = json.loads(Path("assets-data/card_bounds.json").read_text(encoding = "utf8"))
    clown_image: Image = Image.open("assets-data/clown.png")

    for card in Path("output/finished_cards/stats").iterdir():
        if card.is_dir():
            continue

        opened_card: Image = Image.open(card)
        opened_card.paste(clown_image, (bounds_dict["art"]["1"]["x"], bounds_dict["art"]["1"]["y"]))

        # Save card+art
        Path("output/finished_cards").mkdir(exist_ok = True)
        Path("output/finished_cards/clown").mkdir(exist_ok = True)
        opened_card.save(f"output/finished_cards/clown/{card.name}")
