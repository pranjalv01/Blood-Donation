# Generated by Django 2.1.1 on 2018-11-07 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Requestblood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('hospital', models.CharField(max_length=100)),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_email_id', models.EmailField(max_length=254)),
                ('other_message', models.TextField()),
                ('when_required', models.DateField(max_length=8)),
            ],
        ),
    ]
