from django.shortcuts import render
from .models import Student 
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


def student_detail(request):
    stu = Student.objects.get(id=1)
    print(stu)
    serializer = StudentSerializer(stu)
    print(serializer)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data, content_type='application/json')
