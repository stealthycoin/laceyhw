
from django.utils.translation import gettext as _
from django.forms import ModelForm

from models import Source
class SourceForm(ModelForm):
    class Meta:
        model = Source
        fields = ['title']

        labels = {
            'title' : _('Field of Study:'),
        }
from models import Submission
class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ['title', 'summary', 'source', 'other', 'subject']

        labels = {
            'title' : _('I watched:'),
            'summary' : _('Short paragraph about what I learned:'),
            'source' : _('Created By:'),
            'other' : _('Other ideas or thoughts:'),
            'subject' : _('Field of Study:'),
        }
from models import Subject
class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['title']

        labels = {
        }
