"""This module contains the abstract IngestorInterface class.

The IngestorInterface class is the superclass to the Ingestor class.
It provides the abstract parse method that must be implemented
by the subclass.
"""
from abc import ABC, abstractmethod
from typing import List
from QuoteEngine.QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """An abstract base class used for Strategy object design pattern.

    Subclasses of this class will implement parse method for its specific
    file type such as Text, PDF, Docx, and CSV.
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Return True/False if file can be ingested by the instance subclass.

        :param path: Path to file containing motivational quotes.

        :returns bool: True if file can be ingested and False otherwise.
        """
        str_path = str(path)
        ext = str_path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract method which must be implmeneted by subclasses.

        Parses file located at path parameter for the motivational quotes.

        :param path: file path to motiviation quotes file.

        :returns List[QuoteModel]: List of Quote objects in which each Quote object
        represents single record from motivational quote file.
        """
        return
