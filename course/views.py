import datetime

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.shortcuts import get_object_or_404, render
from course.forms import CourseCreateViewForm, TeacherCreateViewForm
from course.models import Course, Category, Teacher


class PageTitleMixin():
    page_title = None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["page_title"] = self.page_title
        return context


class CourseListView(PageTitleMixin, ListView):
    model = Course
    page_title = "Courses"

    def get_queryset(self):
        qs = super().get_queryset()
        courses = Course.objects.filter(
            start__lte=datetime.date.today(),
            status=Course.STATUS_WAIT).only(
            'status',
            'title',
            'description',
            'start',
            'category'
        )
        for course in courses:
            course.status = Course.STATUS_NOW
        courses.bulk_update(courses, ['status'])
        qs = qs.prefetch_related('category')
        return qs


class CourseDetailView(PageTitleMixin, DetailView):
    model = Course
    page_title = "About Course"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.prefetch_related('teachers', 'teachers__profile', 'teachers__profile__user')
        return qs


class CourseCreateView(PageTitleMixin, CreateView):
    model = Course
    success_url = reverse_lazy("course:course_list")
    form_class = CourseCreateViewForm


class CourseUpdateView(PageTitleMixin, UpdateView):
    model = Course
    success_url = reverse_lazy("course:course_list")
    form_class = CourseCreateViewForm


class CourseDeleteView(PageTitleMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('course:course_list')


class CategoryListView(PageTitleMixin, ListView):
    model = Category
    page_title = "Tags"


class CourseListByTagView(View):

    def get(self, request, category_id):
        courses = Course.objects.filter(category=category_id)
        category = get_object_or_404(Category, pk=category_id)

        courses = courses.prefetch_related('category')

        context = {'object_list': courses, 'category': category, 'page_title': f'Tag "{category.category_title}"'}
        return render(request, 'course/course_list_by_tag.html', context=context)


class TeacherListView(PageTitleMixin, ListView):
    model = Teacher
    page_title = "Teachers"

    def get_queryset(self):
        qs = super().get_queryset()
        for teacher in qs:
            teacher.profile.is_teacher = True
            teacher.profile.save()
        qs = qs.prefetch_related('courses').select_related('profile', 'profile__user')
        return qs


class TeacherCreateView(PageTitleMixin, CreateView):
    model = Teacher
    page_title = "Create Teacher"
    form_class = TeacherCreateViewForm
    success_url = reverse_lazy("course:teacher_list")


class TeacherDetailView(PageTitleMixin, DetailView):
    model = Teacher
    page_title = "About Teacher"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.prefetch_related('courses').select_related('profile', 'profile__user')
        return qs


class CourseAPIListView(PageTitleMixin, ListView):
    model = Course
    page_title = "Courses"
    template_name = "course/test.html"
