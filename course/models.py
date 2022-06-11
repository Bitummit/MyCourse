from django.contrib.auth import get_user_model
from django.db import models
from django.utils.functional import cached_property


class Category(models.Model):
    category_title = models.CharField(max_length=50)

    def __str__(self):
        return f"Category {self.category_title}"


class Homework(models.Model):
    title = models.CharField(max_length=50)
    task = models.TextField(blank=True)
    answer_as_text = models.TextField()
    answer_as_file = models.FileField()
    deadline = models.DateTimeField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE)

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
    category = models.ManyToManyField(Category, related_name="course")
    status = models.CharField(choices=STATUS_CHOICES, max_length=16, default=STATUS_WAIT)

    def __str__(self):
        return f"Course {self.title}"

    @cached_property
    def get_short_desc(self):
        return f'{self.description[:20]}...'


class Webinar(models.Model):
    theme = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f"Webinar {self.theme} for {self.course}"


class Teacher(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    about_me = models.TextField(blank=True)


class Student(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    courses = models.ManyToManyField(Course)
    country = models.CharField(max_length=100)



