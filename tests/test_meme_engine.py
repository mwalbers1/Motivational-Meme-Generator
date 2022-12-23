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
    """
    Unit tests for the Meme Generator module
    """

    @classmethod
    def setUpClass(cls) -> None:
        """
        Setup for meme generator tests.
        """
        cls.image_path = "./_data/photos/dog/Tommy_carrot.jpg"

    def test_create_outputfile_name(self):
        meme = MemeEngine('./tmp')
        output_file_name = meme.create_output_filename()
        print(f'output_file_name is {output_file_name}')
        self.assertIsNotNone(output_file_name)

    def test_create_image_meme_text(self):
        """
        Tests image creation from a text motivational quote
        """
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
        """
        Tests image creation from motivational quote in Word document
        """
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
        """
        Test for creating image from PDF motivatonal quote
        """
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
        """
        Test for creating image from motivational quote from CSV file
        """
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

    def tearDown(self) -> None:
        """
        Remove test image files from /tmp folder
        """
        tmp_file_list = ['./tmp/out1.jpg',
                         './tmp/out2.jpg',
                         './tmp/out3.jpg',
                         './tmp/out4.jpg']

        try:
            for tmp_filename in tmp_file_list:
                os.remove(tmp_filename)
        except OSError as oe:
            print(f'Exception raised in removing file: {oe.filename}')
