from .models import Book, Student
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'author', 'bookname', 'bookcount']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        book = serializers.SlugRelatedField(many=True, read_only=True,slug_field='bookname')
        model = Student
        fields = ['id', 'name', 'email', 'password','book']