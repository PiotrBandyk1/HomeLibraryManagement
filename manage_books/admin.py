from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book, Author, Publisher, Series, Note

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Series)
admin.site.register(Note)