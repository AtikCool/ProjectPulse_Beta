from datetime import timezone
from django.urls import reverse
from django.db import models
class Project(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=800)
    start_date = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    members = models.ManyToManyField('users.User')
    
    icon = models.ImageField(upload_to='icons/', blank=True,null=True)
    def get_absolute_url_to_adding(self):
        return f'/add_project/add_task/{self.id}'
    def get_absolute_url(self):
        return f'project/{self.id}'
    def __str__(self):
        return f'{self.name}'

class Task(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=800)
    priority = models.CharField(max_length=50)
    status = models.CharField(blank=True, max_length=20,
                              choices=[('in progress', 'In progress'), ("ended", 'Ended'), ('interruption', "Interruption")], default='In progress')
    deadline = models.DateField()
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, verbose_name='Atik')
    def get_absolute_url(self):
        return f'task/{self.id}'

class Point(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    status = models.BooleanField(default=False)

class Comment(models.Model):
    text = models.TextField()
    date_joined = models.DateTimeField(auto_now_add=True)
    media = models.FileField(blank=True, null=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    task = models.ForeignKey('Task', on_delete=models.CASCADE)



# Create your models here.
