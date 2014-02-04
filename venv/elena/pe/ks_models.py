
from django.contrib.auth.models import User
from django.db import models

class Duration(models.Model):
    time = models.SmallIntegerField()

    def __unicode__(self):
        return '%s min' % (self.time)

class Submission(models.Model):
    duration = models.ForeignKey('Duration')
    date = models.DateField(auto_now=True)
    notes = models.TextField()
    activity = models.ForeignKey('Activity')

    def __unicode__(self):
        return '%s %s' % (self.activity,self.duration)

class Activity(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return '%s' % (self.name)

