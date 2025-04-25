class Book:
  def __init__(self, title, author, pages):
    self.title = title
    self.author = author
    self.num_pages = pages

  def __str__(self):
     return f"{self.title} by {self.author}"

  def __len__(self):
    return self.num_pages

  def __eq__(self, other):
    return self.title == other.title and self.author == other.author

  def __lt__(self, other):
    return self.num_pages < other.num_pages

  def __gt__(self, other):
    return self.num_pages > other.num_pages

  def __add__(self, other):
    return f"{self.num_pages + other.num_pages}"

  def __keyword__(self, keyword):
    return keyword in self.title or keyword in self.author

  def __getitem__(self, key):
    if key == "title":
      return self.title
    elif key == "author":
      return self.author
    elif key == "num_pages":
      return self.num_pages               

book1 = Book("The Hobbit", "J. R. R Tolkien", 350)
book2 = Book("Harry Potter and The Philospher Stone", "J . K Rowley", 235)

print(book1)
print(book2)
print(len(book1))
print(len(book2))
print(book1 == book2)
print(book1 < book2)
print(book1 > book2)
print(book1 + book2)
print(book1.__keyword__("Hobbit"))
print(book2.__keyword__("Potter"))
print(book1.__getitem__("title"))
print(book2.__getitem__("title"))
print(book1.__getitem__("author"))
print(book2.__getitem__("author"))
print(book1.__getitem__("num_pages"))
print(book2.__getitem__("num_pages"))

