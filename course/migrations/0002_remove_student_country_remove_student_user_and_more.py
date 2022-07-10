# Generated by Django 4.0.4 on 2022-07-09 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='country',
        ),
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='user',
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=30)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_teacher', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='profile',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.PROTECT, to='course.userprofile'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='profile',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.PROTECT, to='course.userprofile'),
        ),
    ]
