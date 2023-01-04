"""
The app module runs a Flask server to gernate a captined image.

Invoke the Flask server with this command:

`python app.py`
"""
import random
import os
import requests
import datetime
from flask import Flask, render_template, abort, request

# Import Ingestor and MemeEngine classes
from QuoteEngine.Ingestor import Ingestor
from MemeGenerator.MemeEngine import MemeEngine


app = Flask(__name__)

# create default output image name
outfile_prefix = 'output-image-'
outfile_suffix = datetime.datetime.now().strftime('%Y%m%d-%H%M%d')+'.jpg'
output_fullname = './static/'+outfile_prefix+outfile_suffix

meme = MemeEngine(output_fullname)


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
    imgs_list = []

    # Use the python standard library os class to find all images within the images images_path directory
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

    1. Use requests to save the image from the image_url form param to a temp local file.
    2. Use the meme object to generate a meme using this temp file and the body and author form paramaters.
    3. Remove the temporary saved image.
    """
    tmp_img_path = f'./tmp/{random.randint(0, 100000000)}.jpg'

    image_url = request.form['image_url']
    r = requests.get(image_url, stream=True)

    with open(tmp_img_path, 'wb') as temp_img_file:
        temp_img_file.write(r.content)

    quote_body = request.form['body']
    if quote_body is None:
        quote_body = "Today is a trip to dog park"

    quote_author = request.form['author']
    if quote_author is None:
        quote_author = "Tommy"

    path_meme_img = meme.make_meme(tmp_img_path, quote_body, quote_author)
    os.remove(tmp_img_path)

    # remove leading dot character from path
    url_path_meme_img = path_meme_img.replace("./", "/")

    return render_template('meme.html', path=url_path_meme_img)


if __name__ == "__main__":
    app.run()
