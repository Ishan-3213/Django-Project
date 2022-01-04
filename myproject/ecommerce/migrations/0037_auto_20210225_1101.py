# Generated by Django 3.1.5 on 2021-02-25 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0036_auto_20210225_1058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='quantity',
        ),
        migrations.AddField(
            model_name='products',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
