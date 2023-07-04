from django.shortcuts import render, redirect
from django.views import View
from accounts import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView,LogoutView, PasswordResetView, PasswordChangeView,PasswordResetDoneView,\
    PasswordResetConfirmView,PasswordChangeDoneView,PasswordResetCompleteView
from accounts.forms import UserLoginForm
from accounts.backends import EmailOrLoginUsernameAuthenticationBackend as Email_Login_Backend
from django.contrib import messages


class RegistrationView(View):

    def get(self, request):
        return render(request, template_name="accounts/registration.html", context={"form": forms.UserRegistrationForm()})

    def post(self, request, *args, **kwargs):
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("home")
        return render(request, "accounts/registration.html", {"form": form})


class MyLoginView(View):
    template_name = "accounts/login.html"
    next_page = "/"
    form_class = UserLoginForm

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = self.form_class(request.POST)
        # print(form)
        # print(form.is_valid())
        print(form.data)
        print(form._errors)
        print(form.is_bound)
        if form.is_valid():
            cd = form.cleaned_data
            user = Email_Login_Backend.authenticate(request, username=cd['username'], password=cd['password'])
            print(user)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in!', 'success')
                return redirect('home')
            else:
                messages.error(request, 'Your email or password is incorrect!', 'danger')
        return render(request, self.template_name, {'form': form})




class MyLogoutView(LogoutView):
    template_name = "accounts/logged_out.html"


class MyPasswordResetView(PasswordResetView):
    template_name = "accounts/password_reset_form.html"


class MyPasswordChangeView(PasswordChangeView):
    template_name = "accounts/password_change_form.html"


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = "accounts/password_reset_done.html"


class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "accounts/password_reset_confirm.html"


class MyPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = "accounts/password_change_done.html"


class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "accounts/password_reset_complete.html"
