from django.conf.urls import url
from . import views


app_name='mymusic'
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^(?P<album_id>[0-9]+)/$',views.detail,name='detail'),
    #mymusic/album_id/favorite
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

]