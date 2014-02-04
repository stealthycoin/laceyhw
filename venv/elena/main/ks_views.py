
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template.loader import render_to_string
from middletier import permissionsCheck
from django.http import HttpResponse
from django.contrib import messages


def log(request):
    if not permissionsCheck(request,False,''):
        messages.add_message(request, messages.ERROR, 'Something went wrong man!')
        return HttpResponse('Denied', status=403)
    d = {}
    from mathematics.views import getSubmission
    from mathematics.models import Submission
    qs = Submission.objects.all()
    from django.template import RequestContext
    d['mathList'] = getSubmission(qs)
    from current_events.views import getSubmission
    from current_events.models import Submission
    qs = Submission.objects.all()
    from django.template import RequestContext
    d['currentList'] = getSubmission(qs)
    from science.views import getSubmission
    from science.models import Submission
    qs = Submission.objects.all()
    from django.template import RequestContext
    d['scienceList'] = getSubmission(qs)
    from pe.views import getSubmission
    from pe.models import Submission
    qs = Submission.objects.all()
    from django.template import RequestContext
    d['peList'] = getSubmission(qs)
    return render(request,"log.html",d)

def Science(request):
    if not permissionsCheck(request,False,''):
        messages.add_message(request, messages.ERROR, 'Something went wrong man!')
        return HttpResponse('Denied', status=403)
    d = {}
    from science.forms import SubjectForm
    from django.template import RequestContext
    d['addSubject'] = render_to_string('form.html', {'title':'Add a new field of study', 'description': 'Is the subject you want not in the list? Add it below, and refresh the page. <br> <center>ex. Anthropology, Paleontology, Xenolinguistics, etc.</center>', 'action':'/api/science/Subject/create/','formFields':SubjectForm().as_p()},context_instance=RequestContext(request))
    from science.forms import SubmissionForm
    from django.template import RequestContext
    d['homework'] = render_to_string('form.html', {'title':'What did you watch?', 'description': 'Whether it was from <em>The Shape of Life</em> or a documentary from Netflix, log your science knowledge here.', 'action':'/api/science/Submission/create/','formFields':SubmissionForm().as_p()},context_instance=RequestContext(request))
    return render(request,"Science.html",d)

def PE(request):
    if not permissionsCheck(request,False,''):
        messages.add_message(request, messages.ERROR, 'Something went wrong man!')
        return HttpResponse('Denied', status=403)
    d = {}
    from pe.forms import ActivityForm
    from django.template import RequestContext
    d['addSubject'] = render_to_string('form.html', {'title':'Add a New Activity', 'description': 'Add a new activty, then refresh the page. <br> <center>ex. Unicycle Ride, Bike Ride, Beach, Swimming, etc.</center>', 'action':'/api/pe/Activity/create/','formFields':ActivityForm().as_p()},context_instance=RequestContext(request))
    from pe.forms import SubmissionForm
    from django.template import RequestContext
    d['homework'] = render_to_string('form.html', {'title':'Log Your Activities', 'description': 'What did you do to move your body today?', 'action':'/api/pe/Submission/create/','formFields':SubmissionForm().as_p()},context_instance=RequestContext(request))
    return render(request,"PE.html",d)

def Current(request):
    if not permissionsCheck(request,False,''):
        messages.add_message(request, messages.ERROR, 'Something went wrong man!')
        return HttpResponse('Denied', status=403)
    d = {}
    from current_events.forms import SubmissionForm
    from django.template import RequestContext
    d['homework'] = render_to_string('form.html', {'title':'', 'description': '', 'action':'/api/current_events/Submission/create/','formFields':SubmissionForm().as_p()},context_instance=RequestContext(request))
    return render(request,"Current.html",d)

def MathHistory(request):
    if not permissionsCheck(request,False,''):
        messages.add_message(request, messages.ERROR, 'Something went wrong man!')
        return HttpResponse('Denied', status=403)
    d = {}
    from math_history.forms import SubmissionForm
    from django.template import RequestContext
    d['homework'] = render_to_string('form.html', {'title':'Creation Form', 'description': '', 'action':'/api/math_history/Submission/create/','formFields':SubmissionForm().as_p()},context_instance=RequestContext(request))
    return render(request,"MathHistory.html",d)

def Mathematics(request):
    if not permissionsCheck(request,False,''):
        messages.add_message(request, messages.ERROR, 'Something went wrong man!')
        return HttpResponse('Denied', status=403)
    d = {}
    from mathematics.forms import SubmissionForm
    from django.template import RequestContext
    d['homework'] = render_to_string('form.html', {'title':'', 'description': '', 'action':'/api/mathematics/Submission/create/','formFields':SubmissionForm().as_p()},context_instance=RequestContext(request))
    return render(request,"Mathematics.html",d)

def Home(request):
    if not permissionsCheck(request,False,''):
        messages.add_message(request, messages.ERROR, 'Something went wrong man!')
        return HttpResponse('Denied', status=403)
    d = {}
    return render(request,"Home.html",d)
