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

DEBUG = False

# If DEBUG is set to False you must set at least a hostname in the next list object
ALLOWED_HOSTS = ['']

"""
    Google Analytics
    I used tracking code with subdomains enabled.
    You may have to update subdomains setting to on, in Property/Admin/Tracking
    Info. Otherwise, just copy your tracking code and replace it in base.html
    template.
"""
# Tracking ID
UACODE = 'UA-CODE-EXAMPLE'
# Just 2nd and 1st level domain
DOMAIN = 'example.com'

# Params for statuses/oembed response
PARAMS = '&omit_script=true&hide_media=false'

# Get your keys at: https://dev.twitter.com/apps

CONSUMER_KEY = ''
CONSUMER_SECRET = ''

OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''
