from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView, CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView



class Studentlist(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class Studentcreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class Studentretrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class Studentupdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class Studentdelete(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class Studentlistcreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class Studentretrieveupdate(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class Studentretrieveupdatedestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer