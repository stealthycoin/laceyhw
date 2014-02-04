
from django.utils.translation import gettext as _
from django.forms import ModelForm

from models import Source
class SourceForm(ModelForm):
    class Meta:
        model = Source
        fields = ['title']

        labels = {
        }
from models import Submission
class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ['source', 'title', 'whatDidYouLearn']

        labels = {
            'whatDidYouLearn' : _('What did you learn?'),
        }
