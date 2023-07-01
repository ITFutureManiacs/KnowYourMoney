"""KnowYourMoney URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from budget_manager import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('expense/create/', views.ExpenseCreateView.as_view(), name='expense-create'),
    path('expense/view/', views.ExpenseListView.as_view(), name='expense-list'),
    path('expense/<int:pk>/update/', views.ExpenseUpdateView.as_view(), name='expense-update'),
    path('expense/<int:pk>/delete/', views.ExpenseDeleteView.as_view(), name='expense-delete'),

    path('income/create/', views.IncomeCreateView.as_view(), name='income-create'),
    path('income/view/', views.IncomeListView.as_view(), name='income-list'),
    path('income/<int:pk>/update/', views.IncomeUpdateView.as_view(), name='income-update'),
    path('income/<int:pk>/delete/', views.IncomeDeleteView.as_view(), name='income-delete'),

    path('user/view/', views.UserListView.as_view(), name='user-list'),
    path('user/<int:pk>/update/', views.UserUpdateView.as_view(), name='user-update'),

    path('category/create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('source/create/', views.SourceCreateView.as_view(), name='source-create'),
    path("accounts/", include("accounts.urls"))
    ]

