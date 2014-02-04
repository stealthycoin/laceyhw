from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string

def getSource(args):
    if len(args) == 1:
        return render_to_string('science_Source.html',{ 'obj' : args[0] })
    else:
        return render_to_string('science_SourceList.html',{ 'objs' : args })

def getSubmission(args):
    if len(args) == 1:
        return render_to_string('science_Submission.html',{ 'obj' : args[0] })
    else:
        return render_to_string('science_SubmissionList.html',{ 'objs' : args })

def getSubject(args):
    if len(args) == 1:
        return render_to_string('science_Subject.html',{ 'obj' : args[0] })
    else:
        return render_to_string('science_SubjectList.html',{ 'objs' : args })
