# DJANGO IMPORTS
from django.contrib.auth import login, logout, authenticate
from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect

from Core.forms import LoginForm


class Login(View):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(email, password, "*" * 100)
            user = authenticate(email=email, password=password)
            print(f'USER: {user}')

            if user is not None:
                print(f'USER TYPE: { user.user_type}')
                if user.is_active:
                    login(request, user)
                    request.session['email'] = user.email
                    return redirect('home')
            else:
                messages.add_message(
                    request,
                    messages.WARNING,
                    "Username or Password didn't match! Please try again"
                )
                return redirect('login')
        return render(request, self.template_name, {'form': form})


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        request.session['username'] = None
        return redirect('login')
