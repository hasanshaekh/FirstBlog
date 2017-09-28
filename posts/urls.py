from django.conf.urls import url
from django.contrib import admin

from posts import views as map

from . import views
urlpatterns = [
  url(r'^$', map.post_list),
 url(r'^create/$', map.post_create),
 url(r'^(?P<id>\d+)/$', map.post_detail,name='detail'),

 url(r'^update/$', map.post_update),
 url(r'^delete/$', map.post_delete),
]