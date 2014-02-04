from models import *
from django.core import serializers


#interactions for model Duration
from django.http import HttpResponse
def createDuration(request):
    if request.method == 'POST':
        data = request.POST.copy()
        del data['csrfmiddlewaretoken'] #remove this since it is not a part of the object
        from pe.forms import DurationForm
        form = DurationForm(data)
        if form.is_valid():
            data = form.cleaned_data
            newObject = Duration(**data)
            newObject.save()
            return HttpResponse('\'Succesfully Created\'')
        return HttpResponse('\'Data Unclean\'')

def retrieveDuration(request):
    if request.method == 'POST':
        data = request.POST
        filters = data['filters']
        qs = Duration.objects.filter(**filters)
        return HttpResponse(serializers.serialize([qs]))
    return HttpResponse('Please send data as POST')

def deleteDuration(request):
    if request.method == 'POST':
        data = request.POST
        filters = data['filters']
        qs = Duration.objects.filter(**filters)
        count = 0
        for obj in qs:
            obj.delete()
            count += 1
        return HttpResponse('Deleted %s objects' % count)
    return HttpResponse('Please send data as POST')



#interactions for model Submission
from django.http import HttpResponse
def createSubmission(request):
    if request.method == 'POST':
        data = request.POST.copy()
        del data['csrfmiddlewaretoken'] #remove this since it is not a part of the object
        from pe.forms import SubmissionForm
        form = SubmissionForm(data)
        if form.is_valid():
            data = form.cleaned_data
            newObject = Submission(**data)
            newObject.save()
            return HttpResponse('\'Succesfully Created\'')
        return HttpResponse('\'Data Unclean\'')

def retrieveSubmission(request):
    if request.method == 'POST':
        data = request.POST
        filters = data['filters']
        qs = Submission.objects.filter(**filters)
        return HttpResponse(serializers.serialize([qs]))
    return HttpResponse('Please send data as POST')

def deleteSubmission(request):
    if request.method == 'POST':
        data = request.POST
        filters = data['filters']
        qs = Submission.objects.filter(**filters)
        count = 0
        for obj in qs:
            obj.delete()
            count += 1
        return HttpResponse('Deleted %s objects' % count)
    return HttpResponse('Please send data as POST')



#interactions for model Activity
from django.http import HttpResponse
def createActivity(request):
    if request.method == 'POST':
        data = request.POST.copy()
        del data['csrfmiddlewaretoken'] #remove this since it is not a part of the object
        from pe.forms import ActivityForm
        form = ActivityForm(data)
        if form.is_valid():
            data = form.cleaned_data
            newObject = Activity(**data)
            newObject.save()
            return HttpResponse('\'Succesfully Created\'')
        return HttpResponse('\'Data Unclean\'')

def retrieveActivity(request):
    if request.method == 'POST':
        data = request.POST
        filters = data['filters']
        qs = Activity.objects.filter(**filters)
        return HttpResponse(serializers.serialize([qs]))
    return HttpResponse('Please send data as POST')

def deleteActivity(request):
    if request.method == 'POST':
        data = request.POST
        filters = data['filters']
        qs = Activity.objects.filter(**filters)
        count = 0
        for obj in qs:
            obj.delete()
            count += 1
        return HttpResponse('Deleted %s objects' % count)
    return HttpResponse('Please send data as POST')

