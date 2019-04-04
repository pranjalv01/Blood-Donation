from django.db import models


# Create your models here.


class Searchdonars(models.Model):


    BLOOD_GROUP_CHOICES=(
            ('A Positive','A+'),
            ('A Negative','A-'),
            ('A Unknown','A'),
            ('B Positive','B+'),
            ('B Negative','B-'),
            ('B Unknown','B'),
            ('AB Positive','AB+'),
            ('AB Negative','AB-'),
            ('AB Unknown','AB'),
            ('O Positive','O+'),
            ('O Negative','O-'),
            ('O Unknown','O'),
            ('Unknown','Unknown'),
        )
    blood_group=models.CharField(max_length=1,choices=BLOOD_GROUP_CHOICES,default="Unknown")




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
    city=models.CharField(max_length=1,choices=CITY_CHOICES,default="Delhi")


    def __unicode__(self):
        return self.blood_group



    def __str__(self):
        return self.blood_group
