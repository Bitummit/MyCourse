from django.contrib import admin
from django.urls import path, include

from MyCourse.settings import DEBUG

urlpatterns = [
    path('', include('course.urls', namespace='course')),
    # path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),


]

if DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
