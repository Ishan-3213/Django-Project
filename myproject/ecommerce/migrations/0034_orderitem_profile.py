# Generated by Django 3.1.5 on 2021-02-24 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0033_auto_20210224_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart_item_profile', to='ecommerce.customer'),
        ),
    ]
