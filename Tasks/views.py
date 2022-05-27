from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, User
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='login')
def index(request):
    tasks = Task.objects.filter(user_id=request.user.id).order_by('-id')
    return render(request, 'pages/index.html', {'tasks':tasks})
@login_required(redirect_field_name='login')
def add_task(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        date = request.POST.get('date')
        status = request.POST.get('status')
        add = Task.objects.create(user_id=request.user.id, task=task, date=date, status=status)
        return redirect('home')
    else:
        return render(request, 'pages/add_task.html')

@login_required(redirect_field_name='login')
def finish_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.status = True
    task.save()
    return redirect('home')

@login_required(redirect_field_name='login')
def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('home')
@login_required(redirect_field_name='login')
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