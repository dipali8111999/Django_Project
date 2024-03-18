from django.db import models


class Book(models.Model):
    author = models.CharField(max_length=100)
    bookname = models.CharField(max_length=200)
    bookcount = models.IntegerField()

    def __str__(self):
        return self.bookname


class Student(models.Model):
    name = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book')
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
