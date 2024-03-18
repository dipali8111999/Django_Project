from django.shortcuts import render
from .serializers import BookSerializer, StudentSerializer
from rest_framework import viewsets,status
from .models import Book, Student
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def buy_book(self, request, *args, **kwargs):
        book_id = kwargs.get('pk')
        student_id = request.data.get('student_id')

        if not student_id:
            return Response({'message': 'Student ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            book = Book.objects.get(pk=book_id)
            student = Student.objects.get(pk=student_id)
        except Book.DoesNotExist:
            return Response({'message': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        except Student.DoesNotExist:
            return Response({'message': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

        if book.bookcount <= 0:
            return Response({'message': 'Book out of stock'}, status=status.HTTP_400_BAD_REQUEST)

        student.books.add(book)
        book.bookcount -= 1
        book.save()

        return Response({'message': 'Book purchased successfully'}, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)





