from django.contrib import admin
from contactus.models import *


#class ContactusAdmin(admin.ModelAdmin):
    #contactus_list=('full_name','query_subject','email_id','mobile_no','city')

# Register your models here.

admin.site.register(Contactus)
