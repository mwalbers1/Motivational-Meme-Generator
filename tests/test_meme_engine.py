"""
To run tests from the project root, run:

$ python -m unittest --verbose tests.test_meme_engine

"""
from PIL import Image
from QuoteEngine.Ingestor import Ingestor
from MemeGenerator.MemeEngine import MemeEngine
import unittest
import os


class TestMemeGenerator(unittest.TestCase):
    """Unit tests for the Meme Generator module."""

    @classmethod
    def setUpClass(cls) -> None:
        """Setup for meme generator tests."""
        cls.image_path = "./_data/photos/dog/Tommy_carrot.jpg"

    def test_create_outputfile_name(self):
        """Test creation of random output file name."""
        meme = MemeEngine('./tmp')
        output_file_name = meme.create_output_filename()
        print(f'output_file_name is {output_file_name}')
        self.assertIsNotNone(output_file_name)

    def test_create_image_meme_text(self):
        """Tests image creation from a text motivational quote."""
        quotes = []
        quote_file = './_data/DogQuotes/DogQuotesTXT.txt'
        quotes.extend(Ingestor.parse(quote_file))

        quote = quotes[0]

        # Create new image with meme
        meme_engine = MemeEngine('./tmp/out1.jpg')
        path = meme_engine.make_meme(self.image_path, quote.body, quote.author)

        img = Image.open(path)
        self.assertIsNotNone(img)
        img.close()

    def test_create_image_meme_docx(self):
        """Tests image creation from motivational quote in Word document."""
        quotes = []
        quote_file = './_data/DogQuotes/DogQuotesDOCX.docx'
        quotes.extend(Ingestor.parse(quote_file))

        quote = quotes[0]

        # Create image from docx meme
        meme_engine = MemeEngine('./tmp/out2.jpg')
        path = meme_engine.make_meme(self.image_path, quote.body, quote.author)

        img = Image.open(path)
        self.assertIsNotNone(img)
        img.close()

    def test_create_image_meme_pdf(self):
        """Test for creating image from PDF motivatonal quote."""
        quotes = []
        quote_file = './_data/DogQuotes/DogQuotesPDF.pdf'
        quotes.extend(Ingestor.parse(quote_file))

        quote = quotes[0]

        # Create image from docx meme
        meme_engine = MemeEngine('./tmp/out3.jpg')
        path = meme_engine.make_meme(self.image_path, quote.body, quote.author)

        img = Image.open(path)
        self.assertIsNotNone(img)
        img.close()

    def test_create_image_meme_csv(self):
        """Test for creating image from motivational quote from CSV file."""
        quotes = []
        quote_file = './_data/DogQuotes/DogQuotesCSV.csv'
        quotes.extend(Ingestor.parse(quote_file))

        quote = quotes[0]

        # Create image from docx meme
        meme_engine = MemeEngine('./tmp/out4.jpg')
        path = meme_engine.make_meme(self.image_path, quote.body, quote.author)

        img = Image.open(path)
        self.assertIsNotNone(img)
        img.close()

    def test_flask_app_setup(self):
        """Test setup method from flask app."""
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

        self.assertIsNotNone(quotes_list)
        self.assertIsNotNone(imgs_list)

        self.assertGreater(len(quotes_list), 0)
        self.assertGreater(len(imgs_list), 0)

    def tearDown(self) -> None:
        """Remove test image files from /tmp folder."""
        try:
            for root, _, files in os.walk('./tmp'):
                for file_name in files:
                    full_file_path = os.path.join(root, file_name)
                    if os.path.exists(full_file_path):
                        os.remove(full_file_path)
        except OSError as oe:
            print(f'Exception raised in removing file: {oe.filename}')
