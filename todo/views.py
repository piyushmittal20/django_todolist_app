from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        task = request.POST.get('text', '')
        task = Task(task_name=task)
        task.save()
        return redirect('/')
    return render(request, 'index.html', {'tasks': tasks})

def delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('/')
