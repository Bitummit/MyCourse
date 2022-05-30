from django.forms import ModelForm

from course.models import Course


class ArticleCreateViewForm(ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'duration', 'start', 'price', 'category', 'status')
