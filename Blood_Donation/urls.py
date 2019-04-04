from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from .views import user_login, user_logout, user_success


urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$',views.homepage),

    url(r'^contactus/',include('contactus.urls')),
    url(r'^registerasdonar/',include('registerasdonar.urls')),


    url(r'^requestblood/',include('requestblood.urls')),

    url(r'^searchdonars/',include('searchdonars.urls')),

    url(r'^accounts/',include('accounts.urls')),

    #url(r'^login/$', auth_views.login,{'template_name': 'login/login.html'}),

    #url(r'^logout/$', auth_views.logout)

    url(r'^login/$',user_login,name="user_login"),

    url(r'^success/$',user_success,name="user_success"),

    url(r'^logout/$',user_logout,name="user_logout"),


]


urlpatterns += staticfiles_urlpatterns()
