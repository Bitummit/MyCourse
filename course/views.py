import datetime

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from course.forms import ArticleCreateViewForm
from course.models import Course


class PageTitleMixin():
    page_title = None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["page_title"] = self.page_title
        return context


class CourseListView(PageTitleMixin, ListView):
    model = Course
    page_title = "Courses"

    # @classmethodD
    # def as_view(cls):
    #
    #     courses = Course.objects.all()
    #     for course in courses:
    #         if course.start < datetime.date.today():
    #             course.status = course.STATUS_NOW
    #             course.save()
    #     view = super().as_view()
    #     return view


class CourseDetailView(PageTitleMixin, DetailView):
    model = Course
    page_title = "About Course"


class CourseCreateView(PageTitleMixin, CreateView):
    model = Course
    success_url = reverse_lazy("course:course_list")
    form_class = ArticleCreateViewForm


class CourseDeleteView(PageTitleMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('course:course_list')
