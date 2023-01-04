"""The Meme Engine module is responsible for creating new meme images.

The `MemeEngine` class represents a Meme Engine which has methods for
making a meme.
"""
from PIL import Image, ImageDraw, ImageFont
from PIL.Image import Resampling
from datetime import datetime


class MemeEngine:
    """Meme Engine.

    The meme engine will load an image source file from disk and then transform
    the source image by resizing it to max width of 500px, and add a caption to
    the image with the quote body and author. It then saves it to a new image
    file in an output folder.
    """

    def __init__(self, output_dir):
        """Intialize class instance with output directory for new image.

        :param output_dir: path to new image.
        """
        self.output_dir = output_dir

    def make_meme(self, img_path, message, author, width=500) -> str:
        """Generate image with motiviation text.

        :param img_path: path to original image.
        :param message: motiviational text to apply to image.
        :param author: author of motivational text.
        :param width: width of resized image.

        :return: Output directory to new image file.
        """
        try:
            img = Image.open(img_path)

            if img is None:
                print(f"Invalid image file at {img_path}")
                raise

            if img.size[0] == 0:
                print("Unable to resize zero-sized image")
                raise

            if width is not None:
                ratio = width / float(img.size[0])
                height = int(ratio * float(img.size[1]))
                img = img.resize((width, height), Resampling.NEAREST)

            new_message = ""
            if message is not None:
                new_message = message

            if author is not None:
                new_message += " - " + author

            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
            draw.text((10, 30), new_message, font=font, fill='white')

            img.save(self.output_dir)
            return self.output_dir
        except FileNotFoundError:
            print(f"Image not file not found at {img_path}")
        except Exception as exc:
            print('Exception occurred in make_meme function:', exc)

    def create_output_filename(self):
        """Create full path to new image output file.

        :return: full path of the new image output file.
        """
        prefix_file_name = 'Output-'
        img_extension = ".jpg"

        now = datetime.now()
        output_file_name = prefix_file_name + str(int(round(datetime.timestamp(now)))) + img_extension

        return self.output_dir + '/' + output_file_name
