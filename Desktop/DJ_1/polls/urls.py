from django.conf.urls import patterns, url
from polls.views import  current_datetime, input_data


urlpatterns = patterns('',
    url(r'^time/$', current_datetime),
    url(r'^time/page=(?P<num>[0-9]{10})/$', input_data),
)
"""(?P<num>[0-9]+)/$"""