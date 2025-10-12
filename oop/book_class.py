class Book:
    """A class representing a book with title, author, and publication year."""

    def __init__(self, title, author, year):
        """Initialize a new Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """Return a human-readable string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        print(f"Deleting {self.title}")
