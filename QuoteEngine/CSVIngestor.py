from typing import List
import pandas

from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """
    Responsible for parsing motivational quotes stored in CSV files
    """

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse body and author of motivation quotes from the CSV file located at path parameter. Store each record into
        QuoteModel object which has the body and author properties.

        :param path: Path to the CSV file containing motivational quotes

        returns: List of Quote objects in which each record in file is stored into a quote object
        """
        str_path = str(path)
        if not cls.can_ingest(str_path):
            raise Exception(f"Cannot ingest file type at {path}")

        quotes = []

        try:
            df = pandas.read_csv(path)

            for index, row in df.iterrows():
                new_quote = QuoteModel(row['body'], row['author'])
                quotes.append(new_quote)
        except Exception as excep:
            print(excep)
            print(f"Error occurred in reading file at {path}")

        return quotes
