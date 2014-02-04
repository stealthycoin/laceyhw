
from django.contrib.auth.models import User
from django.db import models

class Submission(models.Model):
    date = models.DateField(auto_now=True)
    description = models.TextField()
    whatDidYouLearn = models.TextField()

    def __unicode__(self):
        return '%s' % (self.description)

