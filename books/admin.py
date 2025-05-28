from django.contrib import admin
from books.models import BookImage, Book, Author, Address, Publisher


# Register your models here.


@admin.register(BookImage)
class BookImageAdmin(admin.ModelAdmin):
    list_display = ["book", "image", "is_cover", "created_at", "updated_at"]
    list_filter = ["is_cover", "created_at", "updated_at"]


class BookImageInline(admin.StackedInline):
    model = BookImage
    extra = 1
    min_num = 1
    max_num = 10
    fields = ["image", "is_cover"]
    readonly_fields = ["created_at", "updated_at"]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "subject",
        "author",
        "publisher",
        "publication_date",
        "isbn",
        "language",
        "pages",
        "description",
    ]
    inlines = [BookImageInline]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["user__username", "biography", "birth_date", "death_date"]
    search_fields = ["user__first_name", "user__last_name"]
    list_filter = ["birth_date", "death_date"]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ["country", "province", "city"]


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "website",
        "email",
    ]

    filter_horizontal = ["address"]
