# Generated by Django 3.1.5 on 2021-02-11 14:45

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0015_profile_shippingadress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.CharField(max_length=100)),
                ('address_2', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=100)),
                ('address_type', models.CharField(max_length=1)),
                ('default', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.userprofileinfo')),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('ordered_date', models.DateTimeField()),
                ('ordered', models.BooleanField(default=False)),
                ('items', models.ManyToManyField(to='ecommerce.OrderItem')),
                ('shipping_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipping_address', to='ecommerce.address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.userprofileinfo')),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='prod_discount_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='prod_details',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='prod_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_img',
            field=models.ImageField(upload_to=''),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='address',
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(default=datetime.datetime(2021, 2, 11, 14, 45, 58, 7849, tzinfo=utc), max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.userprofileinfo'),
        ),
        migrations.DeleteModel(
            name='ShippingAdress',
        ),
    ]
