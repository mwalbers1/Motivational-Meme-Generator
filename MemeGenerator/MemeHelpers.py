"""Helper functions for the MemeGenerator package.

Helper functions called to help create new meme images.
"""
import re
import datetime
import textwrap
import math


def match_jpg_extension(input_str):
    """Matches input string argument for a jpeg extension.

    :param input_str: string from exception message
    :returns: True if ".jpg" pattern found in input parameter
    """
    regex_obj = re.compile('.+\\.jpg')
    result = re.search(regex_obj, input_str)
    if result:
        return True
    else:
        return False


def create_image_filename(folder, prefix):
    """Creates file name for new output image.

    :param folder: parent folder where image is stored i.e. './static/'.
    :param prefix: The filename prefix.

    :returns: new filename for image file.
    """
    suffix = str(datetime.datetime.now().timestamp()).replace('.', '')
    suffix += '.jpg'
    output_filename = folder + prefix + suffix
    return output_filename


def wrap_body_text(body, author, width=500):
    """Wrap body text based on width of image in pixels.
    One character is equivalent to 8 pixels according to
    https://www.unitconverters.net/typography/character-x-to-pixel-x.htm.

    :param body: body caption text
    :param author: author text
    :param width: width of image in pixels

    :return: wrapped text containing body and author.
    """
    # default number of pixels per character
    default_char_pixels = 8

    # offset to account for border edges
    offset = 4

    char_pixels_plus_offset = default_char_pixels + offset
    line_char_width = math.floor(width / char_pixels_plus_offset)

    full_quote = f'{body}\n - {author}'

    wrapper = textwrap.TextWrapper(width=line_char_width)
    formatted_body_text = wrapper.fill(text=full_quote)

    return formatted_body_text
