import json
import os
import sys
from pathlib import Path

from PIL import Image

import Card
import optimized_txt2img_callable


def do_only_art(cards: list, bounds_dict: dict, stats_done = False):
    for card in cards:
        if card.name == "Name":
            continue
        if card.art_description != "":
            # Generate the art
            prompt: str = "Detailed pencil sketch of " + card.art_description + ", correct anatomy, zoomed out, full body visible, sketch, pencil sketch, journal sketch, pencil drawing, sepia, old paper, yellowed paper, no signature, no text"
            # Currently, these dimensions need to be multiples of 64
            height = 412 + 36  # 448
            width = 670 + 34  # 704
            seed = 27  # random.randint(1, 100)
            n_iter = 1
            n_samples = 1
            ddim_steps = 20

            Path("output").mkdir(exist_ok = True)
            Path("output/generated_artwork").mkdir(exist_ok = True)

            output_file = optimized_txt2img_callable.generate_image(prompt = prompt, width = width, height = height, seed = seed, n_iter = n_iter, n_samples = n_samples, ddim_steps = ddim_steps)

            # Copy art to blank card (or stats card if done)
            generated_image: Image = Image.open(Path().cwd() / Path(output_file))
            cropped = generated_image.crop(box = (17, 18, 704 - 17, 448 - 18))

            blank_card_image: Image = Image.open("assets-data/blank_card.png")
            blank_card_image.paste(cropped, (bounds_dict["art"]["1"]["x"], bounds_dict["art"]["1"]["y"]))

            # Save card+art
            Path("output/finished_cards").mkdir(exist_ok = True)
            Path("output/finished_cards/art").mkdir(exist_ok = True)
            blank_card_image.save(f"output/finished_cards/art/{card.name}.png")

            # Save card+art+stats
            if stats_done:
                stats_card_image: Image = Image.open(f"output/finished_cards/stats/{card.name}.png")
                Path("output/finished_cards").mkdir(exist_ok = True)
                Path("output/finished_cards/art_and_stats").mkdir(exist_ok = True)
                stats_card_image.paste(cropped, (bounds_dict["art"]["1"]["x"], bounds_dict["art"]["1"]["y"]))
                stats_card_image.save(f"output/finished_cards/art_and_stats/{card.name}.png")

            print(f"Finished writing art for card {card.name}")


if __name__ == '__main__':
    cards = Card.load_cards()
    bounds_dict: dict = json.loads(Path("assets-data/card_bounds.json").read_text(encoding = "utf8"))

    do_only_art(cards = cards, bounds_dict = bounds_dict)
