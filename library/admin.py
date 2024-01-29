from django.contrib import admin
from .models import Author, Book, IssuedBook, ReservedBook, ReturnedBook

# Register your models here.
admin.site.register(Author),
admin.site.register(Book),
admin.site.register(IssuedBook),
admin.site.register(ReturnedBook),
admin.site.register(ReservedBook)
