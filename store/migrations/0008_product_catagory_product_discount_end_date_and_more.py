# Generated by Django 4.2.7 on 2023-11-16 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_remove_product_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='catagory',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='discount_end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='discount_start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
