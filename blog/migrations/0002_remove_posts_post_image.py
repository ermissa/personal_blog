# Generated by Django 2.0.3 on 2018-04-18 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='post_image',
        ),
    ]