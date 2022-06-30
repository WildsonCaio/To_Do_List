from django.shortcuts import render, redirect
from django.contrib import auth, messages
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
            messages.error(request, 'Usuário ou Senha incorretos.')
            return render(request, 'pages/login.html')

    else:
        return render(request, 'pages/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('pass')
        password_2 = request.POST.get('pass_2')
        
        try:
            if User.objects.get(username=user):
                messages.error(request, 'Usuário com esse nome já existe.')
                return redirect('register')
        
        except:
            if len(user) < 4:    
                messages.error(request, 'Nome de usuário deve conter no mínimo 4 digitos. ')
                return redirect('register')
            
            elif user.strip() == "":
                messages.error(request, 'Nome não pode ser vazio. ')
                return redirect('register')
            
            elif password != password_2:
                messages.error(request, 'Senhas não coincidem')
                return redirect('register')
            
            elif len(password) < 4:    
                messages.error(request, 'A senha deve conter no mínimo 4 digitos. ')
                return redirect('register')
            
            else:
                User.objects.create_user(username=user, password=password)
                return redirect('login')
    else:    
        return render(request, 'pages/register.html')