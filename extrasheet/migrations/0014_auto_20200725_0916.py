# Generated by Django 3.0.7 on 2020-07-25 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extrasheet', '0013_auto_20200723_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club_in',
            name='upload_file',
            field=models.ImageField(blank=True, upload_to='files/'),
        ),
    ]
