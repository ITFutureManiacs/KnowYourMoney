from django.shortcuts import render, redirect
from django.views import View
from accounts import forms
from django.contrib.auth import authenticate, login


class RegistrationView(View):

    def get(self,request):
        return render(request, template_name="registration.html", context={"form": forms.UserRegistrationForm()})

    def post(self, request, *args, **kwargs):
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("home")
        return render(request, "registration.html", {"form": form})
