# Generated by Django 3.1.5 on 2021-02-19 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0016_auto_20210211_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='zip',
        ),
        migrations.RemoveField(
            model_name='order',
            name='ordered_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='products',
            name='product_img',
        ),
        migrations.RemoveField(
            model_name='products',
            name='slug',
        ),
        migrations.AddField(
            model_name='address',
            name='zip_code',
            field=models.IntegerField(default='380015'),
        ),
        migrations.AddField(
            model_name='products',
            name='prod_img',
            field=models.ImageField(default='ecommerce/p1.jpg', upload_to='ecommerce/'),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pic'),
        ),
        migrations.RemoveField(
            model_name='order',
            name='shipping_address',
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.ManyToManyField(related_name='shipping_address', to='ecommerce.Address'),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='address',
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.ManyToManyField(related_name='profile_address', to='ecommerce.Address'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_user', to='ecommerce.userprofileinfo'),
        ),
    ]