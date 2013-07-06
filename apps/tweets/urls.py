from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('apps.tweets.views',
        url(r'^$', 'get_template'),
        url(r'^tweets$', 'get_tweets'),
        url(r'^save$', 'save_tweet'),
        )

