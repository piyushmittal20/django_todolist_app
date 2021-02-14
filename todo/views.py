from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

# Create your views here.

def index(request):
    orderbyList = ['-is_urgent','-id']
    tasks = Task.objects.all().order_by(*orderbyList)
    if request.method == 'POST':
        task = request.POST.get('text', '')
        urge = request.POST.get('is_urge','')
        if urge == 'on':
            urge = True
        else:
            urge = False
        task = Task(task_name=task,is_urgent=urge)
        task.save()
        return redirect('/')
    return render(request, 'index.html', {'tasks': tasks})

def delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('/')
