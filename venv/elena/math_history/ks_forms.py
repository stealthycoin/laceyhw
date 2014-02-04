
from django.utils.translation import gettext as _
from django.forms import ModelForm

from models import Submission
class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ['mainContributor', 'year', 'bigIdea', 'whatDidYouLearn']

        labels = {
            'mainContributor' : _('Main Contributor:'),
            'bigIdea' : _('What\'s the big idea?'),
            'whatDidYouLearn' : _('What did you learn?'),
        }
