# Generated by Django 3.1.5 on 2021-02-23 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0024_order_pname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pname',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
