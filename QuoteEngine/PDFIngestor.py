"""The PDF ingestor module is responsible for parsing motivational quotes from a PDF file.

The PDFIngesor class parses input PDF file(s) for the body and author of each motivational quote
record.
"""
import os
import pathlib
import random
from typing import List
import subprocess

from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Read motivational quotes from PDF file.

    Parse quote records into QuoteModel objects. Each QuoteModel object
    represents a record from the input PDF file.
    """

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse PDF file specified by path parameter.

        :param path: file path of PDF file consisting of the motivational quote records.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        try:
            tmp_path = pathlib.Path(__file__).parent.parent.resolve() / 'tmp'
            tmp = f'{tmp_path}\\{random.randint(0, 1000000)}.txt'

            ret_code = subprocess.call(['pdftotext', '-layout', path, tmp])
            if ret_code == 1:
                raise Exception("pdftotext - Error opening a PDF file.")
            elif ret_code == 2:
                raise Exception("pdftotext - Error opening the output file.")
            elif ret_code == 3:
                raise Exception('pdftotext - Error related to PDF permissions.')
            elif ret_code == 99:
                raise Exception('pdftotext - Other error occurred.')

            quotes = []
            with open(tmp, "r") as file_ref:
                for line in file_ref.readlines():
                    line = line.strip('\n\r').strip()
                    if len(line) > 3:
                        parsed = line.replace('"', "").split(' - ')
                        new_quote = QuoteModel(parsed[0], parsed[1])
                        quotes.append(new_quote)

            os.remove(tmp)
            return quotes
        except FileNotFoundError as fe:
            print(fe)
        except OSError as ose:
            print(ose)
        except Exception as ex:
            print(ex)
