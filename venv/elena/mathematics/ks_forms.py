
from django.utils.translation import gettext as _
from django.forms import ModelForm

from models import Submission
class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ['description', 'whatDidYouLearn']

        labels = {
            'description' : _('What was the lesson about?'),
            'whatDidYouLearn' : _('What did you learn?'),
        }
