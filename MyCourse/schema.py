import graphene
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType

from course.models import Category, Teacher, Course, UserProfile


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'category_title')


class TeacherType(DjangoObjectType):
    class Meta:
        model = Teacher


class CourseType(DjangoObjectType):
    class Meta:
        model = Course


class UserProfileType(DjangoObjectType):
    class Meta:
        model = UserProfile


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(graphene.ObjectType):
    all_categories = graphene.List(CategoryType)
    all_teachers = graphene.List(TeacherType)
    all_courses = graphene.List(CourseType)
    all_users = graphene.List(UserType)
    all_profiles = graphene.List(UserProfileType)

    def resolve_all_categories(self, info):
        return Category.objects.all()

    def resolve_all_teachers(self, info):
        return Teacher.objects.all()

    def resolve_all_courses(self, info):
        return Course.objects.all()


schema = graphene.Schema(query=Query)


'''
Пример запроса

{
  allCourses{
    title,
    price,
    status,
    category{
      id,
      categoryTitle
    }
    teachers{
      id,
      profile{
        isTeacher,
        user{
          firstName,
          lastName
        }
      }
    }
  }
}
'''
