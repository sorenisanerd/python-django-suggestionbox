from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'suggestionbox.views.list_suggestions', name='suggestion_list'),
    url(r'^(?P<top_id>\d+)/$', 'suggestionbox.views.suggestion_detail', name='suggestion_detail'),
)
