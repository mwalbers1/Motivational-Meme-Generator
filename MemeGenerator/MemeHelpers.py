"""Helper functions for MemeGenerator package

Helper functions defined to help in creating new meme images.
"""
import re
import datetime


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
