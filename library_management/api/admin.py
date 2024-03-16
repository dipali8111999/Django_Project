from django.contrib import admin
from .models import Book, Student

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'bookname', 'bookcount']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id', 'name','book', 'email', 'password']