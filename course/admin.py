from django.contrib import admin
from .models import User, Course, Webinar, Student, Teacher, Homework, Category

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Webinar)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Homework)
admin.site.register(Category)