from django import forms
from django.contrib.auth.models import User
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
        fields = ('profile',)


class SendMailForm(forms.Form):
    user_mail = forms.EmailField(label='Your Email', max_length=64)
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(widget=forms.Textarea(), label='Message')

