from django import forms
from django.forms import ModelForm

from course.models import Course, Teacher


class DateInput(forms.DateInput):
    input_type = 'date'


class CourseCreateViewForm(ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'duration', 'start', 'price', 'category', 'teachers')
        widgets = {
            'start': DateInput()
        }


class TeacherCreateViewForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ('user', 'about_me')
