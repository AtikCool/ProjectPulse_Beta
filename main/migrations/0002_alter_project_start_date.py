# Generated by Django 4.2.11 on 2024-03-17 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
