# Generated by Django 3.1.3 on 2020-11-05 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=200)),
                ('Lastname', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('address', models.TextField()),
                ('phonenumber', models.IntegerField()),
                ('city', models.TextField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=100)),
                ('country', models.CharField(choices=[('I', 'INDIA'), ('U', 'USA'), ('C', 'CANADA'), ('P', 'POLAND')], max_length=200)),
            ],
        ),
    ]
