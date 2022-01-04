# Generated by Django 3.1.5 on 2021-02-04 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=200)),
                ('prod_details', models.CharField(max_length=256)),
                ('prod_price', models.FloatField()),
            ],
        ),
    ]