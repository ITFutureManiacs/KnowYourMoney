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
from django.urls import path
from budget_manager import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('income_added/', views.income_added, name='income_added'),
    path('income_update/', views.income_update, name='income_update'),
    path('income_delete/', views.income_delete, name='income_delete_2'),
    path("income/create", views.IncomeCreateView.as_view()),
    path('income/read', views.IncomeReadView.as_view(), name='income_read'),
    path('income/update/<pk>', views.IncomeUpdateView.as_view()),
    path('income/delete/<pk>', views.IncomeDeleteView.as_view()),
]
