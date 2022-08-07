from django.urls import path, include
from . import views

app_name="second_app"
urlpatterns=[
    path('second_app',views.index,name="home"),
    path('second_app/sign_up',views.users,name="form"),
]