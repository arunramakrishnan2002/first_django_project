from django.contrib import admin
from django.urls import path, include
from . import views

app_name="fourth_app"
urlpatterns = [
    path('fourth_app/home',views.index,name="index"),
    path('fourth_app/register',views.register,name="register"),
    path('fourth_app/login',views.user_login,name="user_login"),
    path('fourth_app/logout',views.user_logout,name="user_logout"),
]
