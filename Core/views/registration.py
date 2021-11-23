from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages

from Core.forms import RegistrationForm
from Core.models import User

class Registration(View):
    template_name = 'registration.html'
    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            is_agree = form.cleaned_data.get('is_agree')
            try:
                User.objects.get(email=email)
                messages.error(request, 'Email already exists')
                return redirect('registration')
            except User.DoesNotExist:
                if password1 == password2:
                    user = User.objects.create_user(
                        email=email, password=password1, user_type=1, is_active=True
                    )
                    user.save()
                    messages.success(request, 'Registration Successful')
                    return redirect('login')
                else:
                    messages.error(request, 'Password does not match')
                    return redirect('registration')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
