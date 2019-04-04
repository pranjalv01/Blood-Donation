from django.urls import path
from django.conf.urls import url
from .views import *

app_name='accounts'



urlpatterns = [


    url(r'^login/$',user_login,name="user_login"),

    url(r'^success/$',user_success,name="user_success"),

    url(r'^logout/$',user_logout,name="user_logout"),
]
