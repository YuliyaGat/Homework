from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Platform_usage(models.Model):
    period = models.CharField(max_length=30)
    google = models.IntegerField(default=0)
    facebook = models.IntegerField(default=0)
    youtube = models.IntegerField(default=0)
    tiktok = models.IntegerField(default=0)
    telegram = models.IntegerField(default=0)
    instagram = models.IntegerField(default=0)
    twitter = models.IntegerField(default=0)

class Use_of_the_media_to_get_news(models.Model):
    Year = models.PositiveIntegerField(validators=[MinValueValidator(2015), MaxValueValidator(2023)])
    Social_Networks = models.IntegerField(default=0)
    News_sites = models.IntegerField(default=0)
    Television = models.IntegerField(default=0)
    Radio = models.IntegerField(default=0)
    Print_media = models.IntegerField(default=0)

class Web_sites(models.Model):
    Site = models.CharField(max_length=30)
    Date = models.CharField(max_length=30)
    Monthly_Unique_Visitors = models.IntegerField(default=0)

class Youtube_type(models.Model):
    Title_in_Ukrainian = models.CharField(max_length=30)
    Type_of_channel = models.CharField(max_length=30)
    Link = models.CharField(max_length=30)

class Youtube(models.Model):
    Date = models.CharField(max_length=30)
    Title_in_Ukrainian = models.CharField(max_length=30)
    Subscribers = models.IntegerField(default=0)
    Views = models.IntegerField(default=0)
    New_views_per_period = models.IntegerField(default=0)

class Telegram_type(models.Model):
    Title_in_Ukrainian = models.CharField(max_length=30)
    Type_of_channel = models.CharField(max_length=30)
    Link = models.CharField(max_length=30)
    Link_tg_stat = models.CharField(max_length=30)

class Telegram(models.Model):
    Date = models.CharField(max_length=30)
    Title_in_Ukrainian = models.CharField(max_length=30)
    Subscribers = models.IntegerField(default=0)
    Summ_views_per_month = models.IntegerField(default=0)

