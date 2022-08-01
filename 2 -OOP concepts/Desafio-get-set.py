class Book:

    def __init__(self):
        self._title = ""

    @property
    def title(self):
        # define os getter do title
        return self._title

    @title.setter
    # define o setter do title
    def title(self, title):
        self._title = title


book1 = Book()
book1.title = "Alice in wonderland"
print(book1.title)
# define o novo titulo
book1.title = "Alice"

print(book1.title)
