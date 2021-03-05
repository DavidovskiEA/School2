from django.shortcuts import render
from rest_framework.generics import (CreateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView, UpdateAPIView)
from .models import School, Group, Student
from .serializers import SchoolSerializer, GroupSerializer, StudentSerializer


class SchoolCreateView(CreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class GroupCreateView(CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class StudentCreateView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class SchoolDestroyView(DestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class GroupDestroyView(DestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class StudentDestroyView(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class SchoolRetrieveView(RetrieveAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class GroupRetrieveView(RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class StudentRetrieveView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class SchoolListView(ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class GroupListView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class SchoolUpdateView(UpdateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class GroupUpdateView(UpdateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class StudentUpdateView(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
