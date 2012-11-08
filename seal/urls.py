from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from seal.view import home
admin.autodiscover()

# Index page. DO NOT TOUCH
urlpatterns = patterns('',
    url(r'^/?$', home.index),
    url(r'^redirect/?', home.redirect),
    url(r'^registration/?$', home.register),
    url(r'^logout/?$', home.logout_page),
    url(r'^login/?$', 'django.contrib.auth.views.login'),
)

#urlpatterns += patterns('view.delivery',
#    url(r'^teacher/delivery/newdelivery/(?P<idpractice>\d+)/(?P<idstudent>\d+)?/$', 'newdelivery'),
#    url(r'^teacher/delivery/listdelivery/(?P<idpractice>\d+)/$', 'listdelivery'),
#    url(r'^teacher/delivery/download/(?P<iddelivery>\d+)/$', 'download'),
#)
#
#urlpatterns += patterns('view.practice',
#    url(r'^teacher/practices/?$', 'index'),
#    url(r'^teacher/practices/newpractice/(?P<idcourse>\d+)$', 'newpractice'),
#    url(r'^teacher/practices/editpractice/(?P<idcourse>\d+)/(?P<idpractice>\d+)/$', 'editpractice'),
#    url(r'^teacher/practices/download/(?P<idpractice>\d+)/$', 'download')
#)
#
#urlpatterns += patterns('view.student',
#    url(r'^teacher/students/?$', 'index'),
#    url(r'^teacher/students/home/(?P<idstudent>\d+)$', 'home'),
#    url(r'^teacher/students/newstudent/(?P<idcourse>\d+)$', 'newstudent'),
#    url(r'^teacher/students/editstudent/(?P<idcourse>\d+)/(?P<idstudent>\d+)/$', 'editstudent'),
#    url(r'^teacher/students/practicelist/(?P<idcourse>\d+)/(?P<idstudent>\d+)/$', 'practicelist'),
#)
#
#urlpatterns += patterns('view.course',
#    url(r'^teacher/course/?$', 'index'),
#    url(r'^teacher/course/newcourse/?$', 'newcourse'),
#    url(r'^teacher/course/editcourse/(?P<idcourse>\d+)$', 'editcourse'),
#)
#
#
##Student site: home, list assignments, deliver assignment, etc
#urlpatterns += patterns('view.undergraduate.student',
#    url(r'^undergraduate/?$', 'index'),
#)


urlpatterns += patterns('',
    url(r'^teacher/?', include('view.teacher.urls')),
)

#Student site: home, list assignments, deliver assignment, etc
urlpatterns += patterns('',
    url(r'^undergraduate/?', include('view.undergraduate.urls')),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
