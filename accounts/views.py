from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.http import HttpResponseRedirect

# Create your views here.



def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('user_success'))
        else:
            context["error"] = "Provide valid Credentials!"
            return render(request,"login/login.html",context)
    else:
        return render(request, "login/login.html",context)


def user_success(request):
    context={}
    context['user'] = request.user
    return render(request,"login/success.html",context)


def user_logout(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse('user_login'))
