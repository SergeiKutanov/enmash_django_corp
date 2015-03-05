from django.conf.urls import patterns, url
from news import views

urlpatterns = patterns(
    '',
    url(r'^list/$', views.index, name="news_index"),
)