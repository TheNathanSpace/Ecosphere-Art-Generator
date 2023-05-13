import csv
import os
from pathlib import Path

from PIL import Image

import text_util

font_name = 'arial.ttf'


def load_cards():
    card_csv = Path("assets-data/card_database.csv")
    if not card_csv.exists():
        print(f"Error: card_database.csv does not exist (exiting)")
        exit(-1)

    cards = []
    with open(file = card_csv, newline = '') as opened_file:
        read_file = csv.reader(opened_file)
        for row in read_file:
            new_card = Card(row)
            cards.append(new_card)

    return cards


class Card:

    def __init__(self, traits: list):
        self.set_traits(traits[0], traits[1], traits[2], traits[3], traits[4], traits[5], traits[6], traits[7])

    def set_traits(self, name: str, short_alignment: str, the_type: str, tier: int, cost: int, power: int, health_duration: int, text: str):
        """
        Helper constructor method for initializing from CSV database file
        """
        self.name = name
        self.short_alignment = short_alignment
        self.type = the_type
        self.tier = tier
        self.cost = cost
        self.power = power
        self.health_duration = health_duration
        self.text = text
        self.rarity = None

        self.stats_file_location = f"output/finished_cards/stats/{self.name}.png"

    def write_stats(self, bounds_dict: dict, card_image: Image, alignments: dict):
        text_util.draw_header_text(bounds_dict = bounds_dict, key = "name", text = self.name, card_image = card_image)
        if self.short_alignment != "":
            text_util.draw_text_to_box(bounds_dict = bounds_dict, key = "alignment", text = self.short_alignment, card_image = card_image, centered = True, border = True, alt_color = alignments[self.short_alignment]["color"])
        text_util.draw_header_text(bounds_dict = bounds_dict, key = "type", text = self.type, card_image = card_image)
        text_util.draw_text_to_box(bounds_dict = bounds_dict, key = "tier", text = str(self.tier), card_image = card_image, centered = True)
        text_util.draw_text_to_box(bounds_dict = bounds_dict, key = "cost", text = str(self.cost), card_image = card_image, centered = True)
        text_util.draw_text_to_box(bounds_dict = bounds_dict, key = "power", text = str(self.power), card_image = card_image, centered = True)
        text_util.draw_text_to_box(bounds_dict = bounds_dict, key = "health_duration", text = str(self.health_duration), card_image = card_image, centered = True)
        text_util.draw_paragraph(bounds_dict = bounds_dict, key = "text", text = self.text, max_lines = 5, card_image = card_image)
