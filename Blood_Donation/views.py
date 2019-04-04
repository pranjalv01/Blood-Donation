from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,get_object_or_404
from django.urls import reverse

def homepage(request):
    return render(request,"search_donars.html")


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
