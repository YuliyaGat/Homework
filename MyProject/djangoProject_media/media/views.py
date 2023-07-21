from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
import pandas as pd
import json
from operator import itemgetter
from .models import Platform_usage, Use_of_the_media_to_get_news, Web_sites, Telegram, Youtube

def index(request):
    return render(request, 'media/index.html')

def platform_usage(request):
    platform_usages = Platform_usage.objects.all().values()
    index_=[]
    for data in platform_usages:
      index_.append("")
    df = pd.DataFrame(platform_usages, index=index_)
    mydict = {"df":df.to_html()}
    # df['period'] = pd.to_datetime(df['period'])
    context = {"xAxis": list(df.period), "google": list(df.google), "youtube": list(df.youtube), "facebook": list(df.facebook), "instagram": list(df.instagram), "tiktok": list(df.tiktok), "twitter": list(df.twitter), "telegram": list(df.telegram)}
    return render(request, 'media/platform_usage.html', context)

def use_of_the_media_to_get_news(request):
    use_of_the_media_to_get_news = Use_of_the_media_to_get_news.objects.all().values()
    index_ = []
    for data in use_of_the_media_to_get_news:
        index_.append("")
    df = pd.DataFrame(use_of_the_media_to_get_news, index=index_)
    mydict = {"df": df.to_html()}
    context = {"xAxis": list(df.Year), "Social_Networks": list(df.Social_Networks), "News_sites": list(df.News_sites),
               "Television": list(df.Television), "Radio": list(df.Radio), "Print_media": list(df.Print_media)}
    return render(request, 'media/use_of_the_media.html', context)

def web_sites(request):
    # https: // www.youtube.com / watch?v = JI8YCANhE1Y
    web_sites = Web_sites.objects.all().values()
    index_=[]
    for data in web_sites:
      index_.append("")
    df = pd.DataFrame(web_sites, index=index_)
    json_records = df.reset_index().to_json(orient ='records')
    arr = []
    arr = json.loads(json_records)
    arr.sort(key=itemgetter('Monthly_Unique_Visitors'),reverse = True)
    context = {'df': arr}
    return  render(request,'media/web_sites.html',context)

def telegram(request):
    telegram = Telegram.objects.all().values()
    index_=[]
    for data in telegram:
      index_.append("")
    df = pd.DataFrame(telegram, index=index_)
    json_records = df.reset_index().to_json(orient ='records')
    arr = []
    arr = json.loads(json_records)
    arr.sort(key=itemgetter('Subscribers'),reverse = True)
    arr1=list(filter(lambda x: x['Date'] == '01.06.2023', arr))
    context = {'df': arr1}
    return render(request, 'media/telegram.html', context)

def youtube(request):
    youtube = Youtube.objects.all().values()
    index_=[]
    for data in youtube:
      index_.append(data)
    df = pd.DataFrame(youtube, index=index_)
    json_records = df.reset_index().to_json(orient ='records')
    arr = []
    arr = json.loads(json_records)
    arr.sort(key=itemgetter('Subscribers'),reverse = True)
    arr1=list(filter(lambda x: x['Date'] == '01.06.2023', arr))
    context = {'df': arr1}
    return render(request, 'media/youtube.html', context)

