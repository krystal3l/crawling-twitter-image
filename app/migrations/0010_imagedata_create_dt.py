# Generated by Django 3.0.1 on 2020-01-05 03:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20200105_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagedata',
            name='create_dt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
