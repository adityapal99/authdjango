# Generated by Django 3.1.1 on 2020-09-17 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(upload_to='profile_pics'),
        ),
    ]
