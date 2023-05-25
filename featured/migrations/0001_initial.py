# Generated by Django 3.2.4 on 2023-05-24 20:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0002_alter_post_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured_date', models.DateField(default=django.utils.timezone.now)),
                ('featured_post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
            ],
        ),
    ]
