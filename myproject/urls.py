from django.conf.urls import patterns, include, url
from core.views import *
from django.contrib import admin

urlpatterns = patterns(
    'core.views',
    url(r'^$', 'home', name='home'),
    url(r'^movie/json$', 'movie_list_json', name='movie_list_json'),
    # url(r'^movie/$', 'movie_list', name='movie_list'),
    url(r'^movie/$', MovieList.as_view(), name='movie_list'),
    url(r'^movie/(?P<pk>\d+)/$', MovieDetail.as_view(), name='movie_detail'),
    url(r'^movie/add/$', MovieCreate.as_view(), name='movie_add'),
    url(r'^admin/', include(admin.site.urls)),
)
