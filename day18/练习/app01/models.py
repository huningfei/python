from django.db import models


# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=20)


class Book(models.Model):
    title = models.CharField(max_length=20)
    publisher = models.ForeignKey(to="Publisher")


class Author(models.Model):
    name = models.CharField(max_length=20)
    books = models.ManyToManyField(to="Book", related_name="authors")


class Userinfo(models.Model):
    name=models.CharField(max_length=20)