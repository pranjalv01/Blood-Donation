from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views



app_name = 'contactus'

urlpatterns = [


    url(r'^$',views.contact_us,name='contact'),
    #url(^'contactus/$',views.contact_us),

]
