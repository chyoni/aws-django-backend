from django.urls import path
from user import views

urlpatterns = [
    path('', views.users, name="users"),
    path('login/', views.login, name="login")
]
