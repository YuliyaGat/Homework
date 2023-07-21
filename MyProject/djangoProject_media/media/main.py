import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject_media.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
import json
from django.conf import settings
from django.core.management import call_command
from pprint import pprint
import gspread
from gspread import Cell, Client, Spreadsheet, Worksheet
from media.models import Web_sites, Platform_usage, Use_of_the_media_to_get_news, Youtube_type, Youtube, Telegram_type, Telegram
import pandas as pd
from operator import itemgetter

#https://www.youtube.com/watch?v=9XdNny1DqXE&t=960s


SPREADSHEET_URL = "https://docs.google.com/spreadsheets/d/1SPlALpmKU438BkAkllN-EF0d3wGN1ro8B9fLa4obGgo/edit?pli=1#gid=818841247"

def available_worksheets(sh: Spreadsheet):
    worksheets = sh.worksheets()
    for ws in worksheets:
        print("Worksheet with title", repr(ws.title), "and id", ws.id)

def show_all_values_in_ws(ws: Worksheet):
    list_of_lists = ws.get_all_values()
    print(list_of_lists)
    print("===" * 20)
    for row in list_of_lists:
        print(row)

def show_worksheet(ws: Worksheet):
    list_of_dicts = ws.get_all_records()
    pprint(list_of_dicts)
    return list_of_dicts

def find_comment_by_author(ws: Worksheet):
    cell: Cell = ws.find("tsn.ua")
    print("Found something at row %s and col %s" % (cell.row, cell.col))
    row = ws.row_values(cell.row)
    print(row)

def main():
    gc: Client = gspread.service_account("package.json")
    sh: Spreadsheet = gc.open_by_url(SPREADSHEET_URL)
    # print(sh)
    # available_worksheets
    # ws = sh.sheet1
    # comments_ws = sh.worksheet("WebSites")
    # show_all_values_in_ws(ws)
    # show_worksheet(comments_ws)
    # find_comment_by_author(comments_ws)

def instal_data(str1,str2,str3):
    gc: Client = gspread.service_account("package.json")
    sh: Spreadsheet = gc.open_by_url(SPREADSHEET_URL)
    ws = sh.worksheet(str1)
    data_list=show_worksheet(ws)
    model_data_list = []
    i=1
    for data in data_list:
        dict = {"model":str3, "pk":i, "fields":data}
        i+=1
        model_data_list.append(dict)
    with open(str2, "w") as json_file:
        json.dump(model_data_list, json_file)
    # settings.configure()
    # call_command('loaddata', 'web_sites.json', app_label='media/fixtures')


instal_data("WebSites", "fixtures/web_sites.json", "media.web_sites")
call_command('loaddata', 'web_sites.json')
instal_data("Copy_Platform usage", "fixtures/platform_usage.json", "media.platform_usage")
call_command('loaddata', 'platform_usage.json')
instal_data("Use of the media to get news", "fixtures/use_media.json", "media.use_of_the_media_to_get_news")
call_command('loaddata', 'use_media.json')
instal_data("Copy_YouTube_Type", "fixtures/youtube_type.json", "media.youtube_type")
call_command('loaddata', 'youtube_type.json')
instal_data("Copy_YouTube_Metrics", "fixtures/youtube.json", "media.youtube")
call_command('loaddata', 'youtube.json')
instal_data("Copy_Telegram_Type", "fixtures/telegram_type.json", "media.telegram_type")
call_command('loaddata', 'telegram_type.json')
instal_data("Copy_Telegram_Metrics", "fixtures/telegram.json", "media.telegram")
call_command('loaddata', 'telegram.json')

# def web_sites():
#     web_sites = Web_sites.objects.all().values()
#     index_=[]
#     for data in web_sites:
#       index_.append("")
#     df = pd.DataFrame(web_sites, index=index_)
#     df['Date'] = pd.to_datetime(df['Date'])
#     mydict = {"df":df.to_html()}
#     for i in df:
#         print(list(df.Site))
#
#
# def web_sites():
#     # https: // www.youtube.com / watch?v = JI8YCANhE1Y
#     web_sites = Web_sites.objects.all().values()
#     index_=[]
#     for data in web_sites:
#       index_.append("")
#     df = pd.DataFrame(web_sites, index=index_)
#     json_records = df.reset_index().to_json(orient ='records')
#     arr = []
#     arr = json.loads(json_records)
#     context = {'df': arr}
#     arr.sort(key=itemgetter('Monthly_Unique_Visitors'))
#     print(arr)
#
# web_sites()

# def use_of_the_media_to_get_news():
#     use_of_the_media_to_get_news = Use_of_the_media_to_get_news.objects.all().values()
#     index_=[]
#     for data in use_of_the_media_to_get_news:
#       index_.append("")
#     df = pd.DataFrame(use_of_the_media_to_get_news, index=index_)
#     mydict = {"df":df.to_html()}
#     print(list(df.News_sites))
# use_of_the_media_to_get_news()


# if __name__ == "__main__":
# main()
