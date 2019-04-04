from django.shortcuts import render
from .models import Searchdonars

import operator
from django.db.models import Q

# Create your views here.
def search_donar(request):

    search_list=Searchdonars.objects.create()

    return render(request,'searchdonars/search_donars.html')









"""def search(self):
    if request.method == 'GET':
        blood_group =  request.GET.get('search')
        city = request.GET.get('search')
        try:
            status = Add_prod.objects.filter()
        return render(request,"searchdonars/search.html",{"blood_group":city})
    else:
        return render(request,"searchdonars/search.html",{})"""
