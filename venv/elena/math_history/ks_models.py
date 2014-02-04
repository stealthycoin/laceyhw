
from django.contrib.auth.models import User
from django.db import models

class Submission(models.Model):
    date = models.DateField(auto_now=True)
    mainContributor = models.CharField(max_length=64)
    year = models.CharField(max_length=4)
    bigIdea = models.TextField()
    whatDidYouLearn = models.TextField()

    def __unicode__(self):
        return '%s - %s' % (self.mainContributor,self.year)

