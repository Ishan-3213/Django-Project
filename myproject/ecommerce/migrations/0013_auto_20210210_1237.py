# Generated by Django 3.1.5 on 2021-02-10 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0012_auto_20210210_1218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='cetegory',
            new_name='category',
        ),
    ]
