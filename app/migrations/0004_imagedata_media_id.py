# Generated by Django 3.0.1 on 2020-01-02 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_imagedata'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagedata',
            name='media_id',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
