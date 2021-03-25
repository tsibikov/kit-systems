
class Library(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    librarians = models.ManyToManyField(Librarian)
    books = models.ManyToManyField(Book)
    readers = models.ManyToManyField(Reader)
    shelfs = models.ManyToManyField(Shelf)


class Librarian(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField()
    library = models.ForeignKey(Library)


class Shelf(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    shelf_title = models.CharField()
    books = models.ManyToManyField(Book)
    library = models.ForeignKey(Library)
    genres = models.ManyToManyField(Genre)
    authors = models.ManyToManyField(Author)

    
class Reader(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField()
    reading_books = models.ManyToManyField(Book, blank=True)
    libraries = models.ManyToManyField(Library)


class Book(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField()
    library = models.ForeignKey(Library)
    genres = models.ManyToManyField(Genre)
    authors = models.ManyToManyField(Author)
    where_is = models.Choisefield(choises = [reader, library])
    shelf = models.ForeignKey(Shelf, blank=True)
    reading_by = models.ForeignKey(Reader, blank=True)


class Author(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField()
    books = models.ManyToManyField(Book)
    genres = models.ManyToManyField(Genre)


class Genre(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField()
    books = models.ManyToManyField(Book)
