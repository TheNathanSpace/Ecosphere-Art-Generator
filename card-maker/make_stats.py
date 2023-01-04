import json
from pathlib import Path

from PIL import Image

import Card


def do_only_stats(cards: list, alignments: dict, bounds_dict: dict):
    for card in cards:
        if card.name == "Name":
            continue

        # Load card
        card_image: Image = Image.open("assets-data/blank_card.png")

        card.write_stats(bounds_dict = bounds_dict, card_image = card_image, alignments = alignments)

        # Save written card
        Path("output").mkdir(exist_ok = True)
        Path("output/finished_cards").mkdir(exist_ok = True)
        Path("output/finished_cards/stats").mkdir(exist_ok = True)
        card_image.save(f"output/finished_cards/stats/{card.name}.png")
        print(f"Finished writing stats for card {card.name}")


if __name__ == '__main__':
    cards = Card.load_cards()
    alignments = json.loads(Path("assets-data/alignments_map.json").read_text(encoding = "utf8"))
    bounds_dict: dict = json.loads(Path("assets-data/card_bounds.json").read_text(encoding = "utf8"))

    do_only_stats(cards = cards, alignments = alignments, bounds_dict = bounds_dict)
