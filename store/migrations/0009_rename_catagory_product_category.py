# Generated by Django 4.2.7 on 2023-11-16 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_product_catagory_product_discount_end_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='catagory',
            new_name='category',
        ),
    ]
