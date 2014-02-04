from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string

def getSubmission(args):
    if len(args) == 1:
        return render_to_string('mathematics_Submission.html',{ 'obj' : args[0] })
    else:
        return render_to_string('mathematics_SubmissionList.html',{ 'objs' : args })
