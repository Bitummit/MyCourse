from django.contrib.auth import get_user_model
from django.db import models


class Category(models.Model):
    category_title = models.CharField(max_length=50)


class Homework(models.Model):
    title = models.CharField(max_length=50)
    task = models.TextField(blank=True)
    answer_as_text = models.TextField()
    answer_as_file = models.FileField()
    deadline = models.DateTimeField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE)


class Course(models.Model):
    STATUS_END = "E"
    STATUS_NOW = "N"

    STATUS_CHOICES = [
        (STATUS_END, "Курс пройден"),
        (STATUS_NOW, "Курс идет"),
        ]

    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    duration = models.IntegerField()
    start = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    status = models.CharField(choices=STATUS_CHOICES, max_length=1)


class Webinar(models.Model):
    theme = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField()


class Teacher(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    about_me = models.TextField(blank=True)


class Student(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    courses = models.ManyToManyField(Course)
    country = models.CharField(max_length=100)



