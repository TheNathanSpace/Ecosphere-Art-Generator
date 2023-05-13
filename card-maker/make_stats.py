import json
from pathlib import Path

from PIL import Image

import Card


def do_only_stats(cards: list, alignments: dict, bounds_dict: dict, chosen_rows = None):
    card: Card
    for i, card in enumerate(cards):
        if card.name == "Name":
            continue

        if len(chosen_rows) != 0:
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

    """
    I started working on directly exporting a collage for Tabletop Simulator,
    but abandoned it because it's not really needed (according to Neo).
    """
# def make_collage(cards: list):
#     cards_shaped = []
#     for i in range(0, 10):
#         cards_shaped.append([])
#
#     card: Card
#     for card in cards:
#         card_image: Image = Image.open(card.stats_file_location)
#
#         i, j = 0, 0
#         for h in range(0, 10):
#
#         cards_shaped.append(card_image)
#
#     """Merge two images into one, displayed side by side
#     :param file1: path to first image file
#     :param file2: path to second image file
#     :return: the merged Image object
#     """
#     image1 = Image.open(file1)
#     image2 = Image.open(file2)
#
#     (width1, height1) = image1.size
#     (width2, height2) = image2.size
#
#     result_width = width1 + width2
#     result_height = max(height1, height2)
#
#     result = Image.new('RGB', (result_width, result_height))
#     result.paste(im = image1, box = (0, 0))
#     result.paste(im = image2, box = (width1, 0))
#
#     return result
#


if __name__ == '__main__':
    cards = Card.load_cards()
    alignments = json.loads(Path("assets-data/alignments_map.json").read_text(encoding = "utf8"))
    bounds_dict: dict = json.loads(Path("assets-data/card_bounds.json").read_text(encoding = "utf8"))

    Path("rows_to_export.txt").touch(exist_ok = True)
    chosen_rows = Path("rows_to_export.txt").read_text().replace(" ", "").split(",")
    chosen_rows = [int(x) - 1 for x in chosen_rows]

    do_only_stats(cards = cards, alignments = alignments, bounds_dict = bounds_dict, chosen_rows = chosen_rows)
