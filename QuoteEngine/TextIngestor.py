from typing import List

from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """
    Responsible for reading motivational quotes from Text file
    """

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse body and author of motivation quotes from the Text file located at path parameter. Store each record into
        QuoteModel object which has the body and author properties.

        :param path: Path to the Txt file continaing motivational quotes

        returns: List of Quote objects in which each record in file is stored into a quote object
        """
        quotes = []
        try:
            with open(path, 'r') as file_ref:
                for line in file_ref.readlines():
                    line = line.strip('\n\r').strip()
                    if len(line) > 0:
                        parsed = line.replace('"', "").split(' - ')
                        new_quote = QuoteModel(parsed[0], parsed[1])
                        quotes.append(new_quote)
        except FileNotFoundError as fe:
            print(fe)
        except OSError as ose:
            print(ose)
        except Exception as ex:
            print(ex)

        return quotes
