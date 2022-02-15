from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    return render(request,'index.html')

def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'login.html')
    context['form']=form
    return render(request,'signup.html',context)


def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username OR password is incorrect')
    return render(request,'login.html')

@login_required
def home(request):
    return render(request,'home.html')