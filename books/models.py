from django.db import models
from django.contrib.auth import get_user_model


from core.models import TimeStamp

User = get_user_model()

class BookImage(TimeStamp, models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="book_images/")
    is_cover = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.book.title} - {'Cover' if self.is_cover else 'Image'}"


class Book(TimeStamp, models.Model):
    title = models.CharField(max_length=255)
    subject = models.CharField(max_length=255, null=True, blank=True)
    author = models.ForeignKey(
        "Author", on_delete=models.SET_NULL, null=True, blank=True, related_name="books"
    )
    publisher = models.ForeignKey(
        "Publisher",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="books",
    )
    publication_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)
    language = models.CharField(max_length=50, null=True, blank=True)
    pages = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Author(TimeStamp, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="authors")
    biography = models.TextField(null=True, blank=True)
    birth_date = models.DateField()
    death_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name, self.user.last_name}"


class Address(TimeStamp, models.Model):
    country = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city


class Publisher(TimeStamp, models.Model):
    title = models.CharField(max_length=255, unique=True)
    address = models.ManyToManyField("Address", related_name="publishers")
    website = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.title
