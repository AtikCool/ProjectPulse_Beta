# Generated by Django 4.2.11 on 2024-03-23 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_task_project_alter_task_status_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
