# Generated by Django 4.0.4 on 2022-06-17 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_category_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('Mobile', 'Mobile'), ('Laptop', 'Laptop'), ('ElectronicAccessories', 'Electronic Accessories')], max_length=30),
        ),
    ]