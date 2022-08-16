from rest_framework import routers

from course.api.api_views import (
    TaskViewSet,
    WebinarViewSet,
    CourseViewSet
)

router = routers.DefaultRouter()
router.register("task", TaskViewSet)
router.register("webinar", WebinarViewSet)
router.register("course", CourseViewSet)
