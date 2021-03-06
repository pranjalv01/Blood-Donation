# Generated by Django 2.1.1 on 2018-11-23 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestblood', '0003_auto_20181122_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestblood',
            name='blood_group',
            field=models.CharField(choices=[('A Positive', 'A+'), ('A Negative', 'A-'), ('A Unknown', 'A'), ('B Positive', 'B+'), ('B Negative', 'B-'), ('B Unknown', 'B'), ('AB Positive', 'AB+'), ('AB Negative', 'AB-'), ('AB Unknown', 'AB'), ('O Positive', 'O+'), ('O Negative', 'O-'), ('O Unknown', 'O'), ('Unknown', 'Unknown')], default='Unknown', max_length=1),
        ),
        migrations.AlterField(
            model_name='requestblood',
            name='city',
            field=models.CharField(choices=[('Ahmedabad', 'ahemdabad'), ('Banglore', 'banglore'), ('Chandigarh', 'chandigarh'), ('Chennai', 'chennai'), ('Delhi', 'delhi'), ('Gurgaon', 'gurgaon'), ('Kolkatta', 'kolkatta'), ('Mumbai', 'mumbai'), ('Pune', 'pune'), ('Noida', 'noida')], default='Delhi', max_length=1),
        ),
        migrations.AlterField(
            model_name='requestblood',
            name='contact_no',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
