from typing import List

from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine.CSVIngestor import CSVIngestor
from QuoteEngine.DocxIngestor import DocxIngestor
from QuoteEngine.PDFIngestor import PDFIngestor
from QuoteEngine.TextIngestor import TextIngestor


class Ingestor(IngestorInterface):
    """
    This class encapsulates all the ingestors to provide a single interface to load any suppored file type
    """

    ingestors = [DocxIngestor, CSVIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Calls parse method on on the Ingestor strategy object that can ingest the file specified by the path parameter

        :param path: Path to the source file containing motivational quotes

        :return List[QuoteModel]
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)


