from django.db import models
from django import forms




import datetime

# Create your models here.
class Registerasdonar(models.Model):
    full_name=models.CharField(max_length=100)



    class UserForm(forms.ModelForm):
        password=forms.CharField(widget=forms.PasswordInput())
        confirm_password=forms.CharField(widget=forms.PasswordInput())




    email_id=models.EmailField()


    dob = models.DateField(max_length=8,default="2000-01-01")

    GENDER_CHOICES = (
            ('M', 'Male'),
            ('F', 'Female'),
    )
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES,default="Male")




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
    blood_group=models.CharField(max_length=15,choices=BLOOD_GROUP_CHOICES,default="Unknown")





    weight=models.IntegerField(blank=True, null=True)


    DONATE_BLOOD_CHOICES=(
            ('Yet to denote','Yet_To_Donate'),
            ('Regular Basis','Regular_Basis'),
            ('On need','On_need'),
        )
    donate_blood=models.CharField(max_length=30,choices=DONATE_BLOOD_CHOICES,default="Yet to denote")



    donate_date = models.DateField(blank=True, null=True)



    res_phoneno = models.CharField(max_length=12,blank=True, null=True)





    mobile_no = models.CharField(max_length=12,blank=True, null=True)


    address=models.CharField(max_length=100)

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
    city=models.CharField(max_length=50,choices=CITY_CHOICES,blank=True, null=True)


    def save(self,*args,**kwargs):

        super(Registerasdonar,self).save(*args,**kwargs)




    def __str__(self):
        return self.full_name
