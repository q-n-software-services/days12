# Generated by Django 4.0.6 on 2022-07-21 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homesite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ayyaam',
            name='date',
            field=models.IntegerField(),
        ),
    ]