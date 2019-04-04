from django.shortcuts import render
from .models import Registerasdonar
# Create your views here.



def register_as_donar(request):



    #if request.method == 'POST':

    registerasdonar=Registerasdonar.objects.create()
    registerasdonar.save()
    registerasdonar = Registerasdonar.objects.all()

    return render(request,"registerasdonar/register_as_donar.html",{'registerasdonar':registerasdonar})



def register_list(request):

    registerasdonar = Registerasdonar.objects.all()

    return render(request,"registerasdonar/registerdata.html",{'registerasdonar':registerasdonar})
