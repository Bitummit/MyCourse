from django.contrib import admin
from django.urls import path

import course.views as course

app_name = "course"

urlpatterns = [
    path('', course.CourseListView.as_view(), name="course_list"),
    path('detail/<int:pk>/', course.CourseDetailView.as_view(), name="course_detail"),
    path('create/', course.CourseCreateView.as_view(), name="course_create"),
    path('delete/<int:pk>', course.CourseDeleteView.as_view(), name="course_delete"),
]
