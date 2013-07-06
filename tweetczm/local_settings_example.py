# DATABASES = {'default':
#             {
#              'ENGINE': 'django.db.backends.mysql',
#              'NAME': '',
#              'USER': '',
#              'PASSWORD': '',
#              'HOST': '',
#              'PORT': '',
#              'OPTIONS': {"init_command": "SET storage_engine=InnoDB;", }
#              }
#              }


# DEBUG = False
# If DEBUG is set to False you must set at least a hostname in the next list object
# ALLOWED_HOSTS = ['']


REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

APIURL = 'https://api.twitter.com/1.1/statuses/oembed.json?id='
PARAMS = '&omit_script=true&hide_media=false'

# Get your keys at: https://dev.twitter.com/apps

CONSUMER_KEY = ""
CONSUMER_SECRET = ""

OAUTH_TOKEN = ""
OAUTH_TOKEN_SECRET = ""

