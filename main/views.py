from functools import reduce

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse
from .models import *

from django.utils import timezone as time
from .forms import AddTaskForm, AddProjectForm
from .models import *
from users.models import *
from django.shortcuts import render, HttpResponseRedirect, redirect


def home(request):
    return render(request, 'main/main.html')

@login_required()
def add_project(request):

    if request.method == 'POST':
        form = AddProjectForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            if form.save().deadline > time.now().date():

                instance = form.save()

                id  = instance.id
                return HttpResponseRedirect(f'{Project.objects.get(id=id).get_absolute_url_to_adding()}')
            else:
                return HttpResponseRedirect(reverse('main:main'))
    else:
        form = AddProjectForm()
    context = {'form':form}
    return render(request, 'main/add_project.html', context)
@login_required()
def add_task(request, project_id):
    project = Project.objects.get(id=project_id)
    form_errors ='a'
    if request.method == 'POST':
        #form = AddTaskForm(data=request.POST, dynamic_initial_value=f'{project.name}')
        form = AddTaskForm(data=request.POST, initial={'project':project}, user=request.user, projects=project)
        if form.is_valid():
            instance = form.save()
            points = request.POST.getlist('input[]')
            for point in points:
                point_save = Point(task=Task.objects.get(id=instance.id), description=f'{point}')
                point_save.save()

            return HttpResponseRedirect(reverse('main:main'))
        else:
            form_errors = form.errors

    else:
        form = AddTaskForm(initial={'project':project}, user=request.user, projects=project)
        #form = AddTaskForm(dynamic_initial_value=f'{project.name}')
    context = {'form':form, 'project':project}
    if form_errors != 'a':
        context['errors'] = form_errors
    return render(request, 'main/add_task.html', context)

@login_required()
def project(request, project_id):
    project = Project.objects.get(id=project_id)
    tasks = Task.objects.filter(project=project)
    if request.method == 'POST':
        print('Hello')
        for el in tasks:
            new_status = request.POST.get('status{}'.format(el.id))
            print(new_status)
            print(el.id)
            el.status = new_status
            el.save()
        return redirect('main:main')
    return render(request, 'main/project.html', {'tasks':tasks, 'project':project})
@login_required()
def task(request, task_id ):
    task = Task.objects.get(id=task_id)
    tasks = Task.objects.filter(project=Project.objects.get(id=task.project.id))
    points = Point.objects.filter(task=task)
    context = {
        'task': task, 'points': points, 'tasks': tasks,
    }


    if points:
        completed_points_count = points.filter(status=True).count()
        procent_of_completed = round((completed_points_count / points.count()) * 100)
        context['procent_of_completed'] = procent_of_completed

    if request.method == 'POST':
         input_points = request.POST.getlist('checkbox[]')
         input_points = map(lambda x: int(x), input_points )
         messages.success(request, ('The update was successful'))
         points.update(status=False)
         Point.objects.filter(id__in=input_points).update(status=True)

         return redirect('main:task', task_id)
    else:

        return render(request, template_name='main/task.html', context=context)
@login_required()
def projects_list(request):
    projects = Project.objects.filter(members=request.user)
    return render(request, 'main/projects_list.html', {'projects':projects})

# Create your views here.
