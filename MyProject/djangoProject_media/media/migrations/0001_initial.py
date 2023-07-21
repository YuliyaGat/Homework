# Generated by Django 3.2.20 on 2023-07-21 21:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Platform_usage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(max_length=30)),
                ('google', models.IntegerField(default=0)),
                ('facebook', models.IntegerField(default=0)),
                ('youtube', models.IntegerField(default=0)),
                ('tiktok', models.IntegerField(default=0)),
                ('telegram', models.IntegerField(default=0)),
                ('instagram', models.IntegerField(default=0)),
                ('twitter', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Telegram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.CharField(max_length=30)),
                ('Title_in_Ukrainian', models.CharField(max_length=30)),
                ('Subscribers', models.IntegerField(default=0)),
                ('Summ_views_per_month', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Telegram_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title_in_Ukrainian', models.CharField(max_length=30)),
                ('Type_of_channel', models.CharField(max_length=30)),
                ('Link', models.CharField(max_length=30)),
                ('Link_tg_stat', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Use_of_the_media_to_get_news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(2015), django.core.validators.MaxValueValidator(2023)])),
                ('Social_Networks', models.IntegerField(default=0)),
                ('News_sites', models.IntegerField(default=0)),
                ('Television', models.IntegerField(default=0)),
                ('Radio', models.IntegerField(default=0)),
                ('Print_media', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Web_sites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Site', models.CharField(max_length=30)),
                ('Date', models.CharField(max_length=30)),
                ('Monthly_Unique_Visitors', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Youtube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.CharField(max_length=30)),
                ('Title_in_Ukrainian', models.CharField(max_length=30)),
                ('Subscribers', models.IntegerField(default=0)),
                ('Views', models.IntegerField(default=0)),
                ('New_views_per_period', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Youtube_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title_in_Ukrainian', models.CharField(max_length=30)),
                ('Type_of_channel', models.CharField(max_length=30)),
                ('Link', models.CharField(max_length=30)),
            ],
        ),
    ]