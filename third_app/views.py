from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'third_app/first_page.html',)
def other_page(request):
    return render(request,'third_app/second_page.html',)
 