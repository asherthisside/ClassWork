# Generated by Django 4.0.1 on 2022-03-27 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=50)),
                ('staff_email', models.CharField(max_length=50)),
                ('staff_phone', models.IntegerField()),
            ],
        ),
    ]
