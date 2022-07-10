from django.contrib import admin
from django.urls import path, include

import course.views as course
from course.api.routers import router

app_name = "course"

urlpatterns = [
    path('', course.CourseListView.as_view(), name="course_list"),
    path('course/detail/<int:pk>/', course.CourseDetailView.as_view(), name="course_detail"),
    path('course/update/<int:pk>/', course.CourseUpdateView.as_view(), name="course_update"),
    path('course/create/', course.CourseCreateView.as_view(), name="course_create"),
    path('course/delete/<int:pk>/', course.CourseDeleteView.as_view(), name="course_delete"),

    path('category/', course.CategoryListView.as_view(), name="category_list"),
    path('course_by_tag/<int:category_id>/', course.CourseListByTagView.as_view(), name="course_list_by_tag"),

    path('teachers/', course.TeacherListView.as_view(), name="teacher_list"),
    path('teachers/create/', course.TeacherCreateView.as_view(), name="teacher_create"),
    path('teachers/<int:pk>/', course.TeacherDetailView.as_view(), name="teacher_detail"),

    path('api/', include(router.urls)),
]
