from django.conf.urls import patterns, include, url
from django.contrib import admin
import DailyDiary

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DeeDee.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('DailyDiary.urls')),
)
