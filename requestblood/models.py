from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Requestblood(models.Model):
    patient_name=models.CharField(max_length=100)
    hospital=models.CharField(max_length=100)

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
    blood_group=models.CharField(max_length=100,choices=BLOOD_GROUP_CHOICES,default="Unknown")





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
    city=models.CharField(max_length=100,choices=CITY_CHOICES,default="Delhi")



    doctor_name=models.CharField(max_length=30,blank=True, null=True)


    contact_name=models.CharField(max_length=30)
    other_message=models.TextField(max_length=100)
    contact_email_id=models.EmailField()


    contact_no = models.CharField(max_length=12,blank=True, null=True)





    when_required= models.DateField(max_length=8,blank=True, null=True)


    def __unicode__(self):
        return self.patient_name


    def __str__(self):
        return self.patient_name
