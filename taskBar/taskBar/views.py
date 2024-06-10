from django.shortcuts import render
from task.models import TaskModel
def home(req):
    data = TaskModel.objects.all()
    print(data)
    return render(req, 'home.html', {'data': data})


def tasks(req):
    data = TaskModel.objects.all()
    print(data)
    return render(req, 'tasks.html', {'data': data})