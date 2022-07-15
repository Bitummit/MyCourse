from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView

from MyCourse.settings import DEBUG


graphiql = False
if DEBUG:
    graphiql = True

urlpatterns = [
    path('', include('course.urls', namespace='course')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),

    path("graphql/", GraphQLView.as_view(graphiql=graphiql)),


]

if DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
