# Generated by Django 4.2.11 on 2024-03-16 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=800)),
                ('start_date', models.DateField()),
                ('deadline', models.DateField()),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=800)),
                ('priority', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('in progress', 'In progress'), ('ended', 'Ended'), ('interruption', 'Interruption')], max_length=20)),
                ('deadline', models.DateField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('media', models.FileField(blank=True, null=True, upload_to='')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]