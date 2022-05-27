from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

def user_login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('pass')
        check_user = auth.authenticate(username=user, password=password)
        print(check_user)
        if check_user is not None:
            auth.login(request, check_user)
            return redirect('home')
        else:
            return render(request, 'pages/login.html')

    else:
        return render(request, 'pages/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

#EFETUAR VALIDAÇÕES
def register(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('pass')
        password_2 = request.POST.get('pass_2')
        create = User.objects.create_user(username=user, password=password)
        return redirect('login')
    else:    
        return render(request, 'pages/register.html')