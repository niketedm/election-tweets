from __future__ import unicode_literals
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.core.paginator import Paginator
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext



import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
import json

from apps.tweets.models import Tweet


def get_oauth():
    oauth = OAuth1(settings.CONSUMER_KEY,
                   client_secret=settings.CONSUMER_SECRET,
                   resource_owner_key=settings.OAUTH_TOKEN,
                   resource_owner_secret=settings.OAUTH_TOKEN_SECRET)
    return oauth


@login_required
def get_new(request):

    c = {}
    c.update(csrf(request))

    if request.method == 'POST':
        tweet = request.POST['url']
        tweet = tweet.split('/')[-1:]

        oauth = get_oauth()

        r = requests.get(url=settings.APIURL + tweet[0] + settings.PARAMS,
                         auth=oauth).content

        r = json.loads(r)

        tweet = Tweet(
            tid=tweet[0],
            html=r['html'],
            url=r['url'],
            author=r['author_name']
        )

        tweet.save()

    return render_to_response('new.html', c, RequestContext(request))


def get_tweets(request):
    tweets = Tweet.objects.all().order_by('id').reverse()
    paginator = Paginator(tweets, 5)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        tweets = paginator.page(page)
        has_next = tweets.has_next()
        next = tweets.next_page_number()
    except:
        tweets = paginator.page(paginator.num_pages)
        next = 0
    return render_to_response('tweets.html', {'tweets': tweets,
                                              'has_next': has_next,
                                              'next': next})


def get_template(request):
    return render_to_response('hello.html', RequestContext(request))
