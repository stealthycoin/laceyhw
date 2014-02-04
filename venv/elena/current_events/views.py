from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string

def getSource(args):
    if len(args) == 1:
        return render_to_string('current_events_Source.html',{ 'obj' : args[0] })
    else:
        return render_to_string('current_events_SourceList.html',{ 'objs' : args })

def getSubmission(args):
    if len(args) == 1:
        return render_to_string('current_events_Submission.html',{ 'obj' : args[0] })
    else:
        return render_to_string('current_events_SubmissionList.html',{ 'objs' : args })
