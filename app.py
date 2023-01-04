"""
The app module runs a Flask server to gernate a captined image.

Invoke the Flask server with this command:

`python app.py`
"""
import random
import os
import requests
from flask import Flask, render_template, abort, request

# Import Ingestor and MemeEngine classes
from QuoteEngine.Ingestor import Ingestor
from QuoteEngine.QuoteModel import QuoteModel
from MemeGenerator.MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # Use the Ingestor class to parse all files in the quote_files variable
    quotes_list = []
    for f in quote_files:
        if Ingestor.can_ingest(f):
            quotes_list.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"
    imgs_list = None

    # Use the pythons standard library os class to find all images within the images images_path directory
    for root, _, files in os.walk(images_path):
        for file_name in files:
            imgs_list.append(os.path.join(root, file_name))

    return quotes_list, imgs_list


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme.

    Use the random python standard library class to:
    1. select a random image from imgs array.
    2. select a random quote from the quotes array.
    """
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    out_rel_path = os.path.relpath(path)

    return render_template('meme.html', path=out_rel_path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme.

    # @TODO:
    1. Use requests to save the image from the image_url form param to a temp local file.
    2. Use the meme object to generate a meme using this temp file and the body and author form paramaters.
    3. Remove the temporary saved image.
    """
    path = None

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
