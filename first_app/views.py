from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic,WebPage,AccessRecord

# Create your views here.

def index(request):
    webpages_list=AccessRecord.objects.order_by('date')
    my_dict={
        'insert_here':"Hello I am inserted in this template fom first_app/views.py file",
        'access_records': webpages_list
    }
    return render(request,'first_app/index.html',context=my_dict)
 