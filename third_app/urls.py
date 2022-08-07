from django.contrib import admin
from django.urls import path, include
from . import views
app_name="third_app"
urlpatterns = [
    path('third_app/home',views.index,name="index"),
    path('third_app/other',views.other_page,name="other"),
]
