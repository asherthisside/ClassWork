# Generated by Django 4.0.1 on 2022-04-06 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orm_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang_name', models.CharField(max_length=35)),
            ],
        ),
        migrations.AlterField(
            model_name='toffee',
            name='kid',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='orm_app.kid'),
        ),
        migrations.CreateModel(
            name='Framework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame_name', models.CharField(max_length=35)),
                ('language', models.ForeignKey(default='Unknown Language', on_delete=django.db.models.deletion.SET_DEFAULT, to='orm_app.language')),
            ],
        ),
    ]
