from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.utils.functional import cached_property


class Category(models.Model):
    category_title = models.CharField(max_length=50)

    def __str__(self):
        return f"Category {self.category_title}"


class AnswerTask(models.Model):
    answer_as_text = models.TextField()
    answer_as_file = models.FileField()
    task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='answers')
    student = models.ManyToManyField('Student', related_name='answers')


class Task(models.Model):
    title = models.CharField(max_length=50)
    task = models.TextField(blank=True)
    deadline = models.DateTimeField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return f"Homework {self.title} for {self.course}"


class Course(models.Model):
    STATUS_NOW = "In progress"
    STATUS_WAIT = "Wait for group"

    STATUS_CHOICES = [
        (STATUS_NOW, "Курс идет"),
        (STATUS_WAIT, "Набор группы")
        ]

    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    duration = models.IntegerField()
    start = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ManyToManyField(Category, related_name="courses")
    status = models.CharField(choices=STATUS_CHOICES, max_length=16, default=STATUS_WAIT)
    teachers = models.ManyToManyField('Teacher', related_name='courses', default=None)

    def __str__(self):
        return f"Course {self.title}"

    @cached_property
    def get_short_desc(self):
        return f'{self.description[:20]}...'


class Webinar(models.Model):
    theme = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='webinars')
    date = models.DateTimeField()

    def __str__(self):
        return f"Webinar {self.theme} for {self.course}"


class Teacher(models.Model):
    profile = models.OneToOneField('UserProfile', on_delete=models.PROTECT, default=None, related_name='teacher')
    about_me = models.TextField(blank=True)

    def __str__(self):
        return f'{self.profile.user.first_name} {self.profile.user.last_name}'


class Student(models.Model):
    profile = models.OneToOneField('UserProfile', on_delete=models.PROTECT, default=None, related_name='student')
    courses = models.ManyToManyField(Course, related_name='students')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    location = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username



