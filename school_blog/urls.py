from django.urls import path
from .views import *

app_name = 'School'

urlpatterns = [
    path('school/all', SchoolCreateView.as_view()),
    path('group/all', GroupCreateView.as_view()),
    path('student/all', StudentCreateView.as_view()),
]
