# Generated by Django 3.2.4 on 2023-05-26 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
