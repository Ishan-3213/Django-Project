# Generated by Django 3.1.5 on 2021-02-08 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_userprofileinfo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Products',
        ),
        migrations.DeleteModel(
            name='UserProfileInfo',
        ),
    ]
