# Generated by Django 3.2.4 on 2023-05-09 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_user_kl0k9t', upload_to='images/'),
        ),
    ]
