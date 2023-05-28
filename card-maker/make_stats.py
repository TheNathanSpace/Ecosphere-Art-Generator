import json
from pathlib import Path

from PIL import Image

import Card


def do_only_stats(cards: list, alignments: dict, bounds_dict: dict, chosen_rows = None):
    card: Card
    for i, card in enumerate(cards):
        if card.name == "Name":
            continue

        if chosen_rows is not None and len(chosen_rows) != 0:
            if i not in chosen_rows:
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

    Path("rows_to_export.txt").touch(exist_ok = True)
    chosen_rows = Path("rows_to_export.txt").read_text().replace(" ", "").split(",")
    
    if chosen_rows[0] != '':
        chosen_rows = [int(x) - 1 for x in chosen_rows]
    else:
        chosen_rows = None
        
    do_only_stats(cards = cards, alignments = alignments, bounds_dict = bounds_dict, chosen_rows = chosen_rows)
