from django.contrib import admin

from .models import Author, Book, Genre, Instance, Language, Status

# Register your models here.
admin.site.register(Language)
admin.site.register(Status)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Instance)
