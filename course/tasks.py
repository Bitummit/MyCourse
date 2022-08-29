import time

from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_mail_to_us_task(subject, message, user_email):
    send_mail(
        subject,
        message,
        user_email,
        ['ignat.700@mail.ru'],
        fail_silently=False)


@shared_task
def send_mail_to_user_task(user_email):
    send_mail(
        'Your message received!',
        'Thank you for your message!',
        'ignat.700@mail.ru',
        [user_email],
        fail_silently=False)
