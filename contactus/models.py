from django.db import models
from django.urls import reverse


# Create your models here.
class Contactus(models.Model):
    full_name=models.CharField(max_length=100)

    QUERY_SUBJECT_CHOICES=(
            ('Helpline','help_line'),
            ('Marketing','market'),
            ('Other','other'),
        )
    query_subject=models.CharField(max_length=50,choices=QUERY_SUBJECT_CHOICES,default="Helpline")



    email_id=models.EmailField()


    mobile_no = models.CharField(max_length=12,blank=True, null=True)




    CITY_CHOICES=(
            ('Ahmedabad','ahemdabad'),
            ('Banglore','banglore'),
            ('Chandigarh','chandigarh'),
            ('Chennai','chennai'),
            ('Delhi','delhi'),
            ('Gurgaon','gurgaon'),
            ('Kolkatta','kolkatta'),
            ('Mumbai','mumbai'),
            ('Pune','pune'),
            ('Noida','noida'),
        )
    city=models.CharField(max_length=50,choices=CITY_CHOICES,default="Delhi")





    class Meta:
        db_table = 'contactus'

    #def save(self,*args,**kwargs):

        #super(Contactus,self).save(*args,**kwargs)

    def __str__(self):
        return self.full_name


    #def __unicode__(self):
        #return "{0} {1} {2} {3} {4}".format(self.full_name,self.query_subject,self.email_id,self.mobile_no,self.city)


    #def get_absolute_url(self):
        #return reverse('contactus:contact')
