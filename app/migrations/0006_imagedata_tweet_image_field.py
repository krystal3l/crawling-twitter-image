# Generated by Django 3.0.1 on 2020-01-04 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200102_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagedata',
            name='tweet_image_field',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]