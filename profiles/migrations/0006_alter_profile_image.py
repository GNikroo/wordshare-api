# Generated by Django 3.2.4 on 2023-05-19 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_user_dpyhbv', upload_to='images/'),
        ),
    ]
