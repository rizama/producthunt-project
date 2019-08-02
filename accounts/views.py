from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    # ? Cek Request Method dari User
    if(request.method == 'POST'):
        # * User has info and wants an account Now

        # Cek Password sama atau tidak
        if request.POST['password'] == request.POST['password2']:
            # * Cek Apakah sudah ada username yang terdaftar atau belum
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {
                    'error':'Username has been taken'
                })
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {
                    'error':'Password Must Match'
                }) 
    else:
        # * User wants to enter Info
        return render(request, 'accounts/signup.html')

def signin(request):
    return render(request, 'accounts/signin.html')

def logout(request):
    # TODO : Need to route to homepage
    # TODO : Dont Forget to Logout 
    return render(request, 'accounts/signup.html')