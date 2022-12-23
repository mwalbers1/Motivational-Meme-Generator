from typing import List
import docx

from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """
    Responsible for parsing motiviational quotes stored in Word docx files
    """

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse body and author of motivation quotes from docx file located at path parameter. Store each record into
        QuoteModel object which has the body and author properties.

        :param path: Path to the docx Word file containing the motivational quotes

        returns: List of QuoteModel objects
        """
        if not cls.can_ingest(path):
            raise Exception(f"Cannot ingest file type at {path}")

        quotes = []

        try:
            doc = docx.Document(path)

            for para in doc.paragraphs:
                if para.text != "":
                    parse = para.text.split('-')
                    new_quote = QuoteModel(parse[0], parse[1])
                    quotes.append(new_quote)
        except Exception as exc:
            print(exc)
            print(f"Issue parsing Docx file at {path}")

        return quotes