import os

from PIL import ImageDraw, ImageFont
from PIL.Image import Image

fonts_dir = os.path.join(os.environ['WINDIR'], 'Fonts')
font_name = 'arial.ttf'


def draw_text(image: Image, x: int, y: int, text: str, size: int, fill_color: str, border_color: str | None, border_offset: int):
    """
    Draws text onto an Image, with optional border

    :param image: The Image object
    :param x: Horizontal location
    :param y: Vertical location
    :param text: The text string
    :param size: The font size
    :param fill_color: The text color
    :param border_color: The color to draw the text border (None for no border)
    :param border_offset: The border offset (width)
    """
    draw = ImageDraw.Draw(image)

    font: ImageFont = ImageFont.truetype(font = os.path.join(fonts_dir, font_name), size = size)

    if border_color is not None:
        for i in range(0, border_offset):
            draw.text((x + i, y), text, font = font, fill = border_color)
        for i in range(0, border_offset):
            draw.text((x, y + i), text, font = font, fill = border_color)
        for i in range(0, border_offset):
            draw.text((x - i, y), text, font = font, fill = border_color)
        for i in range(0, border_offset):
            draw.text((x, y - i), text, font = font, fill = border_color)
        corners = 0.6
        for i in range(0, int(border_offset * corners)):
            draw.text((x + i, y + i), text, font = font, fill = border_color)
        for i in range(0, int(border_offset * corners)):
            draw.text((x - i, y - i), text, font = font, fill = border_color)
        for i in range(0, int(border_offset * corners)):
            draw.text((x + i, y - i), text, font = font, fill = border_color)
        for i in range(0, int(border_offset * corners)):
            draw.text((x - i, y + i), text, font = font, fill = border_color)

    # Draw main
    draw.text((x, y), text, font = font, fill = fill_color)


def draw_header_text(bounds_dict: dict, key: str, text: str, card_image: Image):
    """
    Draws text to fit a bounding box. Starting font size, margins, and padding are
    normalized for the header (name/type).

    :param bounds_dict: THe dictionary of bounding boxes
    :param key: The element you're writing in, as the key in bounds_dict
    :param text: The text string to write
    :param card_image: The Image object (loaded in PIL)
    """
    # Get text bounds
    text_x_1 = bounds_dict[key]["1"]["x"]
    text_x_2 = bounds_dict[key]["2"]["x"]

    text_y_1 = bounds_dict[key]["1"]["y"]
    text_y_2 = bounds_dict[key]["2"]["y"]

    delta_x = text_x_2 - text_x_1
    delta_y = text_y_2 - text_y_1

    margin_font_size = 48
    margin_offset = 26
    max_length = int(delta_x - (margin_offset * 2))

    # Decrease font size from the max vertical until it fits horizontally
    font: ImageFont = ImageFont.truetype(font = os.path.join(fonts_dir, font_name), size = margin_font_size)
    while font.getlength(text) > max_length:
        margin_font_size -= 1
        font: ImageFont = ImageFont.truetype(font = os.path.join(fonts_dir, font_name), size = margin_font_size)

    # Center vertically
    y_offset = int((delta_y - margin_font_size) * 0.5)

    draw_text(card_image, text_x_1 + margin_offset, text_y_1 + y_offset, text, margin_font_size, "#000000", None, 0)


def draw_text_to_box(bounds_dict: dict, key: str, text: str, card_image: Image, centered = False, border = False, alt_color = None):
    """
    Draws text to fit a bounding box, using the maximum possible size with no border.

    :param bounds_dict: THe dictionary of bounding boxes
    :param key: The element you're writing in, as the key in bounds_dict
    :param text: The text string to write
    :param card_image: The Image object (loaded in PIL)
    :param centered: Whether to center the text horizontally
    :param border: Whether to use white text with black border
    :param alt_color: The color to put inside the border
    """
    if text == "":
        return

    # Get text bounds
    text_x_1 = bounds_dict[key]["1"]["x"]
    text_x_2 = bounds_dict[key]["2"]["x"]

    text_y_1 = bounds_dict[key]["1"]["y"]
    text_y_2 = bounds_dict[key]["2"]["y"]

    delta_x = text_x_2 - text_x_1
    delta_y = text_y_2 - text_y_1

    # Font should take up 80% of vertical space
    font_80_y = int((text_y_2 - text_y_1) * 0.8)
    font_85_x = int((text_x_2 - text_x_1) * 0.85)
    final_font_y = font_80_y

    # Decrease font size from the max vertical until it fits horizontally
    font: ImageFont = ImageFont.truetype(font = os.path.join(fonts_dir, font_name), size = final_font_y)
    while font.getlength(text) > font_85_x:
        final_font_y -= 1
        font: ImageFont = ImageFont.truetype(font = os.path.join(fonts_dir, font_name), size = final_font_y)

    # Calculate padding
    y_offset = int((delta_y - final_font_y) * 0.5)
    x_offset = int((delta_x - font.getlength(text)) * 0.5)

    if not centered:
        x_offset = y_offset * 1.35

    if not border:
        draw_text(card_image, text_x_1 + x_offset, text_y_1 + y_offset, text, final_font_y, "#000000", None, 0)
    else:
        if alt_color is None:
            draw_text(card_image, text_x_1 + x_offset, text_y_1 + y_offset, text, final_font_y, "#D9D9D9", "#000000", int(final_font_y * 0.095))
        else:
            draw_text(card_image, text_x_1 + x_offset, text_y_1 + y_offset, text, final_font_y, alt_color, "#000000", int(final_font_y * 0.095))


def draw_paragraph(bounds_dict: dict, key: str, text: str, max_lines: int, card_image: Image, centered = False, border = False):
    """
    Draws text to fit a bounding box, using the maximum possible size with no border.
    :param bounds_dict: THe dictionary of bounding boxes
    :param key: The element you're writing in, as the key in bounds_dict
    :param text: The text string to write
    :param max_lines: How many lines to split the paragraph into
    :param card_image: The Image object (loaded in PIL)
    :param centered: Whether to center the text horizontally
    :param border: Whether to use white text with black border
    """

    if text == "":
        return

    # Calculate name position and draw name
    text_x_1 = bounds_dict[key]["1"]["x"]
    text_x_2 = bounds_dict[key]["2"]["x"]

    text_y_1 = bounds_dict[key]["1"]["y"]
    text_y_2 = bounds_dict[key]["2"]["y"]

    delta_x = text_x_2 - text_x_1
    delta_y = text_y_2 - text_y_1

    """
    The basic algorithm here is:
    
    1. Start with a base font size that is always used, if possible.
    2. Add words to the string until font.getlength() is larger than the max width. Move to the next line.
    3. If every line is used and additional space is needed, restart the whole process with a smaller font size.
    
    In this way, the font size will stay consistent most of the time, while still being able to accommodate longer text sections.
    It's not super efficient, but you aren't gonna be running this very often.
    """
    margins = 26
    font_size = 36
    while True:
        padding = int(font_size * 0.45)
        font: ImageFont = ImageFont.truetype(font = os.path.join(fonts_dir, font_name), size = font_size)

        split_lines = []
        current_line = ""
        temp_line = ""
        for word in text.split(" "):
            temp_line += word
            # If too long
            if font.getlength(temp_line) + (margins * 2) > delta_x:
                split_lines.append(current_line)
                current_line = word + " "
                temp_line = current_line
            else:
                temp_line += " "
                current_line = temp_line
        split_lines.append(current_line)

        num_lines = len(split_lines)
        if num_lines * font_size + (num_lines - 1) * padding + margins * 2 <= delta_y:
            break
        else:
            font_size -= 1

    y_point = text_y_1 + margins
    for line in split_lines:
        if not border:
            draw_text(card_image, text_x_1 + margins, y_point, line, font_size, "#000000", None, 0)
        else:
            draw_text(card_image, text_x_1 + margins, y_point, line, font_size, "#D9D9D9", "#000000", int(font_size * 0.095))

        # Move down by one font plus padding
        y_point += font_size + padding
