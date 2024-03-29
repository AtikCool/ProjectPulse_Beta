from django import forms
from django.db.models import Q

from .models import *
from users.models import *
class AddProjectForm(forms.ModelForm):
    name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={
        'type':'text', 'id':'title', 'name':'title',
        'class':"w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500",
        'placeholder':"Enter project title"
    }))
    description = forms.CharField(max_length=800, widget=forms.Textarea(attrs={
        'id': 'description', 'name':'description',
        'class':"w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500",
        'placeholder':'Enter project description', 'rows':'4'
        }))



    deadline = forms.DateField(widget=forms.DateInput(attrs={
        'type':'date', 'id':'date', 'name':'date',
        'class':'w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500'
    }))
    members = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple())
    icon = forms.FileField(widget=forms.FileInput(attrs={
        'name':'icon_input',
        'type':'file',
        'onchange': 'loadFile(event)',
        'class': 'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'
    }))
    class Meta:
        model = Project
        fields = ['name', 'description', 'deadline', 'members', 'icon']
class AddTaskForm(forms.ModelForm):
    name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={
        'type':'text', 'id':'title', 'name':'title',
        'class':"w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500",
        'placeholder':"Enter task's title"
    }))
    description = forms.CharField(max_length=800, widget=forms.Textarea(attrs={
        'id': 'description', 'name':'description',
        'class':"w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500",
        'placeholder':"Enter task's description", 'rows':'4'
        }))

    priority = forms.CharField(max_length=40, widget=forms.TextInput(attrs={
        'type': 'text', 'id': 'priority', 'name': 'priority',
        'class': "w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500",
        'placeholder': "Enter task's priority"
    }))


    project = forms.ModelChoiceField(queryset=Project.objects.all(), widget=forms.Select(attrs={

            'name': 'project', 'id': 'projects',
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-3 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}))
    user = forms.ModelChoiceField(
            queryset=User.objects.all(),
            widget=forms.Select(attrs={
                'name': 'project', 'id': 'projects',
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-3 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}))

    deadline = forms.DateField(widget=forms.DateInput(attrs={
        'type':'date', 'id':'date', 'name':'date',
        'class':'w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500'
    }))

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Получаем значение для фильтрации из переданных аргументов
        projects = kwargs.pop('projects', None)
        super(AddTaskForm, self).__init__(*args, **kwargs)
        if user:



            members = projects.members
            self.fields['user'].queryset = members

    class Meta:
        model = Task
        fields = ['name', 'description', 'priority', 'deadline', 'user', 'project']