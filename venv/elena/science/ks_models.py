
from django.contrib.auth.models import User
from django.db import models

class Source(models.Model):
    title = models.CharField(max_length=30)

    def __unicode__(self):
        return '%s' % (self.title)

class Submission(models.Model):
    title = models.CharField(max_length=64)
    summary = models.TextField()
    source = models.ForeignKey('Source')
    other = models.TextField()
    date = models.DateField(auto_now=True)
    subject = models.ForeignKey('Subject')

    def __unicode__(self):
        return '%s from %s' % (self.title,self.source)

class Subject(models.Model):
    title = models.CharField(max_length=30)

    def __unicode__(self):
        return '%s' % (self.title)

