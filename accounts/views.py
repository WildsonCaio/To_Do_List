from django.shortcuts import render, redirect
from django.contrib import auth

def user_login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('pass')
        check_user = auth.authenticate(username=user, password=password)
        print(check_user)
        if check_user is not None:
            return redirect('home')
        else:
            return render(request, 'pages/login.html')

    else:
        return render(request, 'pages/login.html')
