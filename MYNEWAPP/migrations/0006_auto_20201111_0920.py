# Generated by Django 3.1.3 on 2020-11-11 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MYNEWAPP', '0005_auto_20201111_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerdetails',
            name='email',
            field=models.EmailField(default='NA', max_length=254),
        ),
    ]
