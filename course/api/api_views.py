
from rest_framework import viewsets


from course.api.serializers import TaskSerializer, WebinarSerializer

from course.models import Task, Webinar


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class WebinarViewSet(viewsets.ModelViewSet):
    queryset = Webinar.objects.all()
    serializer_class = WebinarSerializer



