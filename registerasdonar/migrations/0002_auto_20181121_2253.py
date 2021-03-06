# Generated by Django 2.1.1 on 2018-11-21 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registerasdonar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(choices=[('Ahmedabad', 'ahemdabad'), ('Banglore', 'banglore'), ('Chandigarh', 'chandigarh'), ('Chennai', 'chennai'), ('Delhi', 'delhi'), ('Gurgaon', 'gurgaon'), ('Kolkatta', 'kolkatta'), ('Mumbai', 'mumbai'), ('Pune', 'pune'), ('Noida', 'noida')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Clientc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_no', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Clientv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_phoneno', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Donate_blood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donate_blood', models.CharField(choices=[('Yet to denote', 'Yet_To_Donate'), ('Regular Basis', 'Regular_Basis'), ('On need', 'On_need')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Your_bloodgroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group', models.CharField(choices=[('A Positive', 'A+'), ('A Negative', 'A-'), ('A Unknown', 'A'), ('B Positive', 'B+'), ('B Negative', 'B-'), ('B Unknown', 'B'), ('AB Positive', 'AB+'), ('AB Negative', 'AB-'), ('AB Unknown', 'AB'), ('O Positive', 'O+'), ('O Negative', 'O-'), ('O Unknown', 'O'), ('Unknown', 'Unknown')], max_length=1)),
            ],
        ),
        migrations.DeleteModel(
            name='Foo',
        ),
        migrations.RenameField(
            model_name='registerasdonar',
            old_name='full_name1',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='registerasdonar',
            name='city',
        ),
        migrations.RemoveField(
            model_name='registerasdonar',
            name='email_id1',
        ),
        migrations.RemoveField(
            model_name='registerasdonar',
            name='mobile_no',
        ),
        migrations.RemoveField(
            model_name='registerasdonar',
            name='query_subject',
        ),
        migrations.AddField(
            model_name='registerasdonar',
            name='donate_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
