from django.shortcuts import render, redirect
from . import forms
from .  import models

# Create your views here.
def add_task(req):
    if req.method == "POST":
        addTask = forms.TaskForm(req.POST)
        if addTask.is_valid():
            addTask.save()
            return redirect('showtasks')
    else:
        addTask = forms.TaskForm()
    return render(req, 'add_task.html', {'form' : addTask})

def edit_task(req, id):
    print(id)
    task = models.TaskModel.objects.get(pk=id)
    taskForm = forms.TaskForm(instance=task)

    if req.method == "POST":
        taskForm = forms.TaskForm(req.POST, instance=task)
        if taskForm.is_valid():
            taskForm.save()
            return redirect('showtasks')
    return render(req, 'add_task.html', {'form' : taskForm})


def delete_task(req, id):
    task = models.TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('showtasks')