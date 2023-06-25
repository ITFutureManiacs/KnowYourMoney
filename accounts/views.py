from django.shortcuts import render
from django.views import View
from accounts import forms


class RegistrationView(View):

    def get(self,request):
        return render(request, template_name="registration.html", context={"form": forms.UserRegistrationForm()})