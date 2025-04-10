from django.shortcuts import render, redirect
from apps.users.forms import LoginForms, RegisterForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.
def login(request):
    form = LoginForms()


    if request.method =='POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            name=form['name_login'].value()
            password=form['password'].value()

        user = auth.authenticate(
            request,
            username=name,
            password=password
        )
        if user is not None:
            auth.login(request, user)
            messages.success(request, f"{name} logado(a) com sucesso!")

            return redirect ('index')
        else:
            messages.error(request, "Erro ao efetuar login.")

            return redirect('login')

    return render(request, 'users/login.html', {'form': form})

def register(request):
    form = RegisterForms()

    if request.method =='POST':
        form = RegisterForms(request.POST)

        if form.is_valid():
            name=form['name_register'].value()
            email=form['email'].value()
            password=form['password_1'].value()

            if User.objects.filter(username=name).exists():
                messages.error(request, "Usuário já existente.")

                return redirect('register')
            
            user = User.objects.create_user(
                username=name,
                email=email,
                password=password,
            )
            user.save()
            messages.success(request, "Cadastro efetuado com sucesso!")

            return redirect('login')

    return render(request, 'users/register.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request,'Logout efetuado com sucesso!')

    return redirect('login')