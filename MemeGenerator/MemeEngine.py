"""The Meme Engine module is responsible for creating new meme images.

The `MemeEngine` class represents a Meme Engine which has methods for
making a meme.
"""
from random import randint
from PIL import Image, ImageDraw, ImageFont
from PIL.Image import Resampling
import MemeGenerator.MemeHelpers as MemeHelpers


class MemeEngine:
    """Meme Engine.

    The meme engine will load an image source file from disk and then transform
    the source image by resizing it to max width of 500px, and add a caption to
    the image with the quote body and author. It then saves it to a new image
    file in an output folder.
    """

    def __init__(self, output_dir):
        """Intialize class instance with output path for new image.

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
            with Image.open(img_path) as img:
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

                # Combine body and author into single wrapped text message
                new_message = MemeHelpers.wrap_body_text(body=message,
                                                         author=author,
                                                         width=width)

                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf',
                                          size=20)

                x = randint(5, 10)
                y = randint(5, 100)
                draw.text((x, y), new_message, font=font, fill='white')

                img.save(self.output_dir)

            return self.output_dir
        except FileNotFoundError:
            raise FileNotFoundError(f'Image file not found at {img_path}')
        except Exception as exc:
            raise
