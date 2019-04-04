from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [

    #url(r'^$',views.request_blood,name='request'),

    url(r'^$',views.request_blood),
    url(r'requestlist/$',views.request_list),
]
