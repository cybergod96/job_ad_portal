# Generated by Django 2.1a1 on 2018-06-06 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobad', '0005_remove_advertisement_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyform',
            name='reply',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]