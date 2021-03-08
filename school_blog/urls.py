from django.urls import path
from .views import *

app_name = 'School'

urlpatterns = [
    path('school/all', SchoolCreateView.as_view()),
    path('group/all', GroupCreateView.as_view()),
    path('student/all', StudentCreateView.as_view()),
    path('school/all', SchoolListView.as_view()),
    path('group/all', GroupListView.as_view()),
    path('student/all', StudentListView.as_view()),
    path('school/all', SchoolRetrieveView.as_view()),
    path('group/all', GroupRetrieveView.as_view()),
    path('student/all', StudentRetrieveView.as_view()),
    path('school/all', SchoolDestroyView.as_view()),
    path('group/all', GroupDestroyView.as_view()),
    path('student/all', StudentDestroyView.as_view()),
    path('school/all', SchoolUpdateView.as_view()),
    path('group/all', GroupUpdateView.as_view()),
    path('student/all', StudentUpdateView.as_view()),
]
