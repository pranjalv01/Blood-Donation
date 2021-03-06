# Generated by Django 2.1.1 on 2018-11-23 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0005_auto_20181122_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='city',
            field=models.CharField(choices=[('Ahmedabad', 'ahemdabad'), ('Banglore', 'banglore'), ('Chandigarh', 'chandigarh'), ('Chennai', 'chennai'), ('Delhi', 'delhi'), ('Gurgaon', 'gurgaon'), ('Kolkatta', 'kolkatta'), ('Mumbai', 'mumbai'), ('Pune', 'pune'), ('Noida', 'noida')], default='Delhi', max_length=50),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='query_subject',
            field=models.CharField(choices=[('Helpline', 'help_line'), ('Marketing', 'market'), ('Other', 'other')], default='Helpline', max_length=50),
        ),
    ]
