# Generated by Django 4.0.1 on 2022-04-06 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm_app', '0003_shirt_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='kid',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
