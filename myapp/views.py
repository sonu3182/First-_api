from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializers
from .models import Student
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('first_name')
    serializer_class = StudentSerializers
# Create your views here.
