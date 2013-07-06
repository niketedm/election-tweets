from django.db import models

# Create your models here.

class Tweet(models.Model):

    tid = models.BigIntegerField('Tweet ID', unique=True)
    html = models.TextField('HTML')
    url = models.URLField('URL')
    author = models.CharField('Author', max_length=64)

    def __unicode__(self):
        return str(self.tid) +': '+ self.author
        