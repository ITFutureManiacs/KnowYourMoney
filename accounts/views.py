from django.shortcuts import render, redirect
from django.views import View
from accounts import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView,LogoutView, PasswordResetView, PasswordChangeView,PasswordResetDoneView,\
    PasswordResetConfirmView,PasswordChangeDoneView,PasswordResetCompleteView


class RegistrationView(View):

    def get(self,request):
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


class MyLoginView(LoginView):
    template_name = "accounts/login.html"
    next_page = "/"


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
