from django.urls import path, include
from users.views import *
app_name = 'main'
from .views import *
urlpatterns=[
 path('', home, name='main'),
 path('friends/', friends_list, name='friends'),
 path('projects_list/', projects_list, name='projects_list'),
 path('add_project', add_project, name='add_project'),
 path('add_project/add_task/<int:project_id>', add_task, name='add_task'),
 path('projects_list/project/<int:project_id>', project, name='project'),
 path('projects_list/project/task/<int:task_id>', task, name='task')
]