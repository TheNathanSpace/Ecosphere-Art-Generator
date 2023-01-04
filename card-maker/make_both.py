import json
from pathlib import Path

import Card
from card_maker import make_stats, make_art


def do_both(cards: list, alignments: dict, bounds_dict: dict):
    make_stats.do_only_stats(cards = cards, alignments = alignments, bounds_dict = bounds_dict)
    print(f"Finished writing stats for all cards; moving on to art")

    make_art.do_only_art(cards = cards, bounds_dict = bounds_dict, stats_done = True)
    print(f"Finished writing art for all cards.")


if __name__ == '__main__':
    cards = Card.load_cards()
    alignments = json.loads(Path("assets-data/alignments_map.json").read_text(encoding = "utf8"))
    bounds_dict: dict = json.loads(Path("assets-data/card_bounds.json").read_text(encoding = "utf8"))

    do_both(cards = cards, alignments = alignments, bounds_dict = bounds_dict)
