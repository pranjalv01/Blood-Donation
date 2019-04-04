from django.shortcuts import render

from django.http import HttpResponse
import pymysql
from .models import Requestblood

# Create your views here.



def request_blood(request):

    requestblood = Requestblood.objects.create()
    requestblood.save()

    #if request.user.is_authenticated():
        #user = request.user

    #if request.method == 'POST':


        #form = Requestlist(request.POST)
        #if form.is_valid():
            #form.save(commit=false)

            #form.save()
            #return redirect('/requestblood')
    #else:
        #form = Requestlist() # add this if you want it to automatically fill the form with the old data if there is any.



    #request_list=Requestblood.objects.create()


    return render(request,"requestblood/request_blood.html")


def request_list(request):
    requestblood = Requestblood.objects.all()


    return render(request,"requestblood/requestdata.html",{'requestblood':requestblood})
