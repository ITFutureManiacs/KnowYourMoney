from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LogoutView,
    PasswordResetView,
    PasswordChangeView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordChangeDoneView,
    PasswordResetCompleteView,
)
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView

from accounts import forms
from accounts.backends import (
    EmailOrLoginUsernameAuthenticationBackend as Email_Login_Backend,
)
from accounts.models import CustomUser
from accounts.forms import UserLoginForm, UpdateUserForm


class RegistrationView(View):
    def get(self, request):
        return render(
            request,
            template_name="accounts/registration.html",
            context={"form": forms.UserRegistrationForm()},
        )

    def post(self, request, *args, **kwargs):
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
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
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST, data=request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = Email_Login_Backend.authenticate(
                request, username=cd["username"], password=cd["password"]
            )

            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in!", "success")
                return redirect("home")
            else:
                messages.error(
                    request, "Your email or password is incorrect!", "danger"
                )
        return render(request, self.template_name, {"form": form})


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


class UserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = "accounts/user_list.html"
    fields = ["username", "first_name", "last_name", "email"]


class UserUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UpdateUserForm
    model = CustomUser
    template_name = "accounts/user_update.html"
    success_url = reverse_lazy("user-list")

    def get_initial(self):
        initial_values = super().get_initial()
        initial_values["username"] = self.request.user.username
        initial_values["first_name"] = self.request.user.first_name
        initial_values["last_name"] = self.request.user.last_name
        initial_values['"email"'] = self.request.user.email
        return initial_values
