from django.urls import path
from accounts import views
from accounts import forms

urlpatterns = [
    path('login/', views.MyLoginView.as_view(authentication_form=forms.UserLoginForm), name='login'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path("logout/", views.MyLogoutView.as_view(), name='logout'),
    path("password_change/", views.MyPasswordChangeView.as_view(), name='password_change'),
    path("password_change/done/", views.MyPasswordChangeDoneView.as_view(), name='password_change_done'),
    path("password_reset/", views.MyPasswordResetView.as_view(template_name="accounts/password_reset_form.html"), name='password_reset'),
    path("password_reset/done/", views.MyPasswordResetDoneView.as_view(), name='password_reset_done'),
    path("reset/<uidb64>/<token>/", views.MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path("reset/done/", views.MyPasswordResetCompleteView.as_view(), name='password_reset_complete')
    ]