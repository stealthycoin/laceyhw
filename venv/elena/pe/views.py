from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string

def getDuration(args):
    if len(args) == 1:
        return render_to_string('pe_Duration.html',{ 'obj' : args[0] })
    else:
        return render_to_string('pe_DurationList.html',{ 'objs' : args })

def getSubmission(args):
    if len(args) == 1:
        return render_to_string('pe_Submission.html',{ 'obj' : args[0] })
    else:
        return render_to_string('pe_SubmissionList.html',{ 'objs' : args })

def getActivity(args):
    if len(args) == 1:
        return render_to_string('pe_Activity.html',{ 'obj' : args[0] })
    else:
        return render_to_string('pe_ActivityList.html',{ 'objs' : args })
