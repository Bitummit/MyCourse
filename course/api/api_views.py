from rest_framework import viewsets
from course.api.serializers import (
    TaskSerializer,
    WebinarSerializer,
    CourseSerializer
)
from course.models import (
    Task,
    Webinar,
    Course
)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class WebinarViewSet(viewsets.ModelViewSet):
    queryset = Webinar.objects.all()
    serializer_class = WebinarSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

