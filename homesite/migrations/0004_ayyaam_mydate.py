# Generated by Django 4.0.6 on 2022-07-21 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homesite', '0003_remove_ayyaam_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='ayyaam',
            name='mydate',
            field=models.IntegerField(default=0),
        ),
    ]
