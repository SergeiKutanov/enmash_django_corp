from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from enmashcorp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_action, name='login'),
    url(r'^logout/$', views.logout_action, name='logout'),
    url(r'^contacts/', include('contacts.urls')),
    url(r'^filestorage/', include('filestorage.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
