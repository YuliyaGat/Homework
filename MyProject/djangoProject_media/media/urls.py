from django.urls import path
from . import views

app_name = "media"
urlpatterns = [
    path("", views.index, name="start"),
    path("platform_usage/", views.platform_usage, name="platform_usage"),
    path("use_of_the_media/", views.use_of_the_media_to_get_news, name="use_of_the_media"),
    path("web_sites/", views.web_sites, name="web_sites"),
    path("telegram/", views.telegram, name="telegram"),
    path("youtube/", views.youtube, name="youtube"),

]