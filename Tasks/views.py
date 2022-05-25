from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, User

def index(request):
    tasks = Task.objects.filter(user_id=request.user.id).order_by('-id')
    return render(request, 'pages/index.html', {'tasks':tasks})

def add_task(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        date = request.POST.get('date')
        status = request.POST.get('status')
        add = Task.objects.create(user_id=request.user.id, task=task, date=date, status=status)
        return redirect('home')
    else:
        return render(request, 'pages/add_task.html')


def finish_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.status = True
    task.save()
    return redirect('home')


def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('home')

def edit_task(request, id):
    
    if request.method == 'POST':
        task = get_object_or_404(Task, id=id)
        
        task_2 = request.POST.get('task')
        date = request.POST.get('date')
        status = request.POST.get('status')
        task.task = task_2
        task.status = status
        task.save()
        return redirect('home')
    
    else:
        task = get_object_or_404(Task, id=id)
        return render(request, 'pages/edit_task.html', {'task':task})