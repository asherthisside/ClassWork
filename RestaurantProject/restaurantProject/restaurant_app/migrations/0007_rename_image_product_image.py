# Generated by Django 4.0.4 on 2022-05-28 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0006_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Image',
            new_name='image',
        ),
    ]
