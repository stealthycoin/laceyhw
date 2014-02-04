
from django.contrib.auth.models import User
from django.db import models

class Source(models.Model):
    title = models.CharField(max_length=30)

    def __unicode__(self):
        return '%s' % (self.title)

class Submission(models.Model):
    date = models.DateField(auto_now=True)
    source = models.ForeignKey('Source')
    title = models.CharField(max_length=64)
    whatDidYouLearn = models.TextField()

    def __unicode__(self):
        return '%s' % (self.title)

