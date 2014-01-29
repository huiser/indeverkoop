from django.conf.urls import patterns, url

from .views import WoningList

urlpatterns = patterns('',
	# ex: /polls/
	url(r'^$', WoningList.as_view(), name='woning_index'),
    # ex: /polls/5/
    #url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    ## ex: /polls/5/vote/
    #url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)