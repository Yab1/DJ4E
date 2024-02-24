from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)


class Cat(models.Model):
    name = models.CharField(max_length=128)


class Dog(models.Model):
    name = models.CharField(max_length=128)
