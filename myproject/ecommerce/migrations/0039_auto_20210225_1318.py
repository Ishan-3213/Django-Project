# Generated by Django 3.1.5 on 2021-02-25 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0038_orderitem_quan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='address',
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.ManyToManyField(related_name='customer_Addresses', to='ecommerce.Address'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quan',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
