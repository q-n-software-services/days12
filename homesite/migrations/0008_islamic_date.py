# Generated by Django 4.0.6 on 2022-07-23 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homesite', '0007_suggestons'),
    ]

    operations = [
        migrations.CreateModel(
            name='islamic_date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_islamic', models.IntegerField(default=0)),
                ('month_islamic', models.CharField(max_length=200)),
                ('date_georgian', models.IntegerField(default=0)),
                ('month_georgian', models.IntegerField(default=0)),
            ],
        ),
    ]