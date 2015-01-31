from django.conf.urls import patterns, include, url
from DailyDiary.views import MainIndex
from DailyDiary.views import posted
#from django.auth import accounts

urlpatterns = patterns('',
    url(r'^$', MainIndex.as_view(), name='index_view'),
    url(r'^posted', 'posted')
    #url(r'^accounts/', include('accounts.urls')),
)