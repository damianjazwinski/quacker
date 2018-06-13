from django.shortcuts import render, redirect
from application.forms import RegisterForm
from django.contrib.auth import login, authenticate, logout as auth_logout

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            passwd = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=passwd)
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'authentication/register.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('index')

