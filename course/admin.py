from django.contrib import admin
from .models import Course, Webinar, Student, Teacher, Category, UserProfile, Task, AnswerTask

admin.site.register(Course)
admin.site.register(Webinar)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Task)
admin.site.register(AnswerTask)
admin.site.register(Category)
admin.site.register(UserProfile)
