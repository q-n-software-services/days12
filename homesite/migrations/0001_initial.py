# Generated by Django 4.0.6 on 2022-07-21 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ayyaam',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=1200)),
                ('date', models.IntegerField(max_length=2)),
                ('month', models.CharField(max_length=2)),
                ('month_islamic_title', models.CharField(max_length=22)),
                ('details_page_link', models.CharField(max_length=112)),
            ],
        ),
    ]
