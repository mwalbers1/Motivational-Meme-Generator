"""Quote model module has one class called QuoteModel."""


class QuoteModel:
    """Contains properties for the body and author of a motivational quote."""

    def __init__(self, quote_body, quote_author):
        """Initialize QuoteModel object.

        Initialize the quote body and quote author instance variables to the
        parameters passed into this method.

        :param quote_body: Body of motivational quote.
        :param quote_author: Author of motivational quote.
        """
        self.quote_body = quote_body
        self.quote_author = quote_author

    @property
    def body(self):
        """Property for motivational Quote body."""
        return self.quote_body

    @property
    def author(self):
        """Property for motivational Quote Author."""
        return self.quote_author

    def __repr__(self):
        """System representation of model object."""
        return f'<{self.quote_body}, {self.quote_author}>'

    def __str__(self):
        """Print contents of model instance as `body text - author`."""
        return f'{self.quote_body} - {self.quote_author}'
