# Generated by Django 2.1.1 on 2018-11-07 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='A',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('query_subject', models.TextField()),
                ('email_id', models.EmailField(max_length=254)),
                ('mobile_no', models.IntegerField()),
                ('city', models.TextField()),
            ],
        ),
    ]