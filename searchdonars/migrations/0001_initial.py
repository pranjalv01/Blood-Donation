# Generated by Django 2.1.1 on 2018-11-21 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bloodgroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group', models.CharField(choices=[('A Positive', 'A+'), ('A Negative', 'A-'), ('A Unknown', 'A'), ('B Positive', 'B+'), ('B Negative', 'B-'), ('B Unknown', 'B'), ('AB Positive', 'AB+'), ('AB Negative', 'AB-'), ('AB Unknown', 'AB'), ('O Positive', 'O+'), ('O Negative', 'O-'), ('O Unknown', 'O'), ('Unknown', 'Unknown')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(choices=[('Ahmedabad', 'ahemdabad'), ('Banglore', 'banglore'), ('Chandigarh', 'chandigarh'), ('Chennai', 'chennai'), ('Delhi', 'delhi'), ('Gurgaon', 'gurgaon'), ('Kolkatta', 'kolkatta'), ('Mumbai', 'mumbai'), ('Pune', 'pune'), ('Noida', 'noida')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Searchdonars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]