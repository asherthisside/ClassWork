# Generated by Django 4.0.4 on 2022-05-28 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0005_remove_orderitem_product_orderitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]