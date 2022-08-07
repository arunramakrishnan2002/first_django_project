from django.shortcuts import render
from .forms import NewUserForm

# Create your views here.
def index(request):
    return render(request,'second_app/index.html')

def users(request):
    form=NewUserForm()
    if request.method=="POST":
        form=NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Form Invalid")
    return render(request,'second_app/forms.html',{'form':form})
    
