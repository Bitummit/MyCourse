import datetime

from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.shortcuts import get_object_or_404, render
from course.forms import ArticleCreateViewForm
from course.models import Course, Category


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


class CourseCreateView(PageTitleMixin, CreateView):
    model = Course
    success_url = reverse_lazy("course:course_list")
    form_class = ArticleCreateViewForm


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

        context = {'object_list': courses, 'category': category}
        return render(request, 'course/course_list_by_tag.html', context=context)

