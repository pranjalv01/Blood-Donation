
from .models import Contactus

from django.shortcuts import render,get_object_or_404
from django.urls import reverse





# Create your views here.
def contact_us(request):
    #form=ContactusForm()




    """"if request.Post:
        form=ContactusForm(request.Post)
        if form.is_valid():
            contactus = form.save()"""


    #if request.method == 'POST':

    contactus=Contactus.objects.create()
    contactus.save()
    
    #contact_list = Contactus.objects.all()



    return render(request,"contactus/c_details.html",{'contactus': contactus})
