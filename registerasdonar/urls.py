from django.urls import path
from django.conf.urls import url
from . import views



urlpatterns = [

    url(r'^$',views.register_as_donar),

    url(r'registerlist/$',views.register_list),
]
