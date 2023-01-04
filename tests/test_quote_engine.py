"""
To run tests from the project root, run:

$ python -m unittest --verbose tests.test_quote_engine

"""
import collections.abc
import pathlib
import unittest

from QuoteEngine.CSVIngestor import CSVIngestor
from QuoteEngine.DocxIngestor import DocxIngestor
from QuoteEngine.PDFIngestor import PDFIngestor
from QuoteEngine.TextIngestor import TextIngestor

TEST_DOG_CSV_FILE = pathlib.Path(__file__).parent.parent.resolve() / '_data' / 'DogQuotes' / 'DogQuotesCSV.csv'
TEST_DOG_DOCX_FILE = pathlib.Path(__file__).parent.parent.resolve() / '_data' / 'DogQuotes' / 'DogQuotesDOCX.docx'
TEST_DOG_PDF_FILE = pathlib.Path(__file__).parent.parent.resolve() / '_data' / 'DogQuotes' / 'DogQuotesPDF.pdf'
TEST_DOG_TXT_fILE = pathlib.Path(__file__).parent.parent.resolve() / '_data' / 'DogQuotes' / 'DogQuotesTXT.txt'


class TestQuoteEngine(unittest.TestCase):
    """
    Unit tests for the Quote Engine Module.

    TestQuoteEngine includes tests for the CSV, Docx, PDF, and Text
    Strategy Ingestor objects.
    """

    @classmethod
    def setUpClass(cls) -> None:
        """Intialize Quote models for each type of motiviation file."""
        cls.csv_quotes = CSVIngestor.parse(TEST_DOG_CSV_FILE)
        cls.docx_quotes = DocxIngestor.parse(TEST_DOG_DOCX_FILE)
        cls.pdf_quotes = PDFIngestor.parse(TEST_DOG_PDF_FILE)
        cls.txt_quotes = TextIngestor.parse(TEST_DOG_TXT_fILE)

    @classmethod
    def get_first_or_none(cls):
        """Tests that each collection has at least one item."""
        try:
            next(iter(cls.csv_quotes))
            next(iter(cls.docx_quotes))
            next(iter(cls.pdf_quotes))
            next(iter(cls.txt_quotes))
        except StopIteration:
            return None

    def test_quotes_are_collection(self):
        """Tests CSV quotes is a collection type."""
        self.assertIsInstance(self.csv_quotes, collections.abc.Collection)

    def test_quotes_are_collection_docx(self):
        """Tests Docx quotes is a collection type."""
        self.assertIsInstance(self.docx_quotes, collections.abc.Collection)

    def test_quotes_are_collection_pdf(self):
        """Tests PDF quotes is a collection type."""
        self.assertIsInstance(self.pdf_quotes, collections.abc.Collection)

    def test_quotes_are_collection_txt(self):
        """Tests Text quotes is a collection type."""
        self.assertIsInstance(self.txt_quotes, collections.abc.Collection)

    def test_quotes_contains_all_elements(self):
        """Tests that CSV quotes collection contains all quotes."""
        self.assertEqual(len(self.csv_quotes), 2)

    def test_quotes_contains_all_elements_docx(self):
        """Tests that Docx quotes collection contains all quotes."""
        self.assertEqual(len(self.docx_quotes), 4)

    def test_quotes_contains_all_elements_pdf(self):
        """Tests that PDF quotes collection contains all quotes."""
        self.assertEqual(len(self.pdf_quotes), 3)

    def test_quotes_contains_all_elements_txt(self):
        """Tests that Text quotes collection contains all quotes."""
        self.assertEqual(len(self.txt_quotes), 3)
