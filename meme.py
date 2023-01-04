"""
This module is executed from the terminal command line.

The meme module is run from the terminal by invoking `python meme.py`. The script takes three optional CLI
arguments:

--body: a string quote body
--author: a string quote author
--path: path to a source image
"""
import os
import random
import argparse
import datetime

# Import Ingestor and MemeEngine classes
from QuoteEngine.Ingestor import Ingestor
from QuoteEngine.QuoteModel import QuoteModel
from MemeGenerator.MemeEngine import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    # create default output image name
    outfile_prefix = 'output-image-'
    outfile_suffix = datetime.datetime.now().strftime('%Y%m%d-%H%M%d')+'.jpg'
    output_fullname = './tmp/'+outfile_prefix+outfile_suffix

    meme = MemeEngine(output_fullname)
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # Use ArgumentParser to parse the following CLI arguments.
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    parser = argparse.ArgumentParser(description="Meme Generator from command line.")
    parser.add_argument('--body', type=str, help='Specify meme body.')
    parser.add_argument('--author', type=str, help='Specify author.')
    parser.add_argument('--path', type=str, help='Specify path to source image.')

    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
