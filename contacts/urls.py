from django.conf.urls import patterns, url

from contacts import views

urlpatterns = patterns(
    '',
    url(r'^services/$', views.index, name='contacts_index'),
    url(r'^(?P<contact_id>\d+)/$', views.viewContact, name='contact_detail'),
    url(r'^service/$', views.viewServices, name='contact_services'),
    url(r'^service/(?P<service_id>\d+)/$', views.viewService, name='contact_service_detail'),
    url(r'^search/$', views.searchContact, name='contact_search'),
)