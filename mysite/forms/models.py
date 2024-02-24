from enum import unique
from django.db import models


# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=200, unique=True)


class Status(models.Model):
    name = models.CharField(max_length=13, unique=True)


class Genre(models.Model):
    name = models.CharField(max_length=13, unique=True)


class Author(models.Model):
    name = models.CharField(max_length=13, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)


class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    isbn = models.CharField(max_length=13, unique=True)
    author = models.ManyToManyField(Author)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)


class Instance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    due_date = models.DateField(null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
