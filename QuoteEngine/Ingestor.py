"""Contains Ingestor class which serves as a container object of each type of ingestor oject.

The Ingestor class holds a collection of ingestors for each file type (docx,csv,pdf,txt). Ingestor class then
calls parse method for the ingestor object that's responsible for parsing the file located at path
parameter.
"""
from typing import List

from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine.CSVIngestor import CSVIngestor
from QuoteEngine.DocxIngestor import DocxIngestor
from QuoteEngine.PDFIngestor import PDFIngestor
from QuoteEngine.TextIngestor import TextIngestor


class Ingestor(IngestorInterface):
    """Ingestor class inherits from the IngestorInterface abstract class.

    Ingestor class encapsulates all the ingestors to provide a single interface to load any
    suppored file type.
    """

    ingestors = [DocxIngestor, CSVIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Call parse method on the Ingestor strategy object for specific file specified by the path parameter.

        :param path: Path to the source file containing motivational quotes.

        :return List[QuoteModel].
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)


