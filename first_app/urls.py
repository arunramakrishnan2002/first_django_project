from django.urls import path, include
from . import views

app_name="first_app"
urlpatterns=[
    path('first_app',views.index,name="index"),
]