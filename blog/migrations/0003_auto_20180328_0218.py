# Generated by Django 2.0.3 on 2018-03-28 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180326_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post_image',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
