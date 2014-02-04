
from django.conf.urls import include, patterns, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url('^api/math_history/Submission/create/$','math_history.middletier.createSubmission',name='create_Submission'),
    url('^api/current_events/Source/create/$','current_events.middletier.createSource',name='create_Source'),
    url('^api/current_events/Submission/create/$','current_events.middletier.createSubmission',name='create_Submission'),
    url('^api/science/Source/create/$','science.middletier.createSource',name='create_Source'),
    url('^api/science/Submission/create/$','science.middletier.createSubmission',name='create_Submission'),
    url('^api/science/Subject/create/$','science.middletier.createSubject',name='create_Subject'),
    url('^api/pe/Duration/create/$','pe.middletier.createDuration',name='create_Duration'),
    url('^api/pe/Submission/create/$','pe.middletier.createSubmission',name='create_Submission'),
    url('^api/pe/Activity/create/$','pe.middletier.createActivity',name='create_Activity'),
    url('^api/mathematics/Submission/create/$','mathematics.middletier.createSubmission',name='create_Submission'),
    url('^api/login/$','main.middletier.login',name='login'),
    url('^api/logout/$','main.middletier.logout',name='logout'),
    url('^api/signup/$','main.middletier.signup',name='signup'),
    url('^log/$','main.views.log',name='log'),
    url('^science/$','main.views.Science',name='Science'),
    url('^pe/$','main.views.PE',name='PE'),
    url('^current/$','main.views.Current',name='Current'),
    url('^mathhistory/$','main.views.MathHistory',name='MathHistory'),
    url('^math/$','main.views.Mathematics',name='Mathematics'),
    url('^$','main.views.Home',name='Home'),
)
