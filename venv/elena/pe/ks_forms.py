
from django.utils.translation import gettext as _
from django.forms import ModelForm

from models import Duration
class DurationForm(ModelForm):
    class Meta:
        model = Duration
        fields = ['time']

        labels = {
        }
from models import Submission
class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ['duration', 'notes', 'activity']

        labels = {
            'notes' : _('What did you do?'),
        }
from models import Activity
class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['name']

        labels = {
            'name' : _('New Activity:'),
        }
