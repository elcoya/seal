from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Index page. DO NOT TOUCH
urlpatterns = patterns('view.home',
    #(r'^$', 'direct_to_template', {'template': 'index.html'}),
    url(r'^/?$', 'index'),
)

urlpatterns += patterns('view.practice',
    url(r'^practices/?$', 'index'),
    url(r'^practices/newpractice/(?P<idcourse>\d+)$', 'newpractice'),
    url(r'^practices/editpractice/(?P<idcourse>\d+)/(?P<idpractice>\d+)/$', 'editpractice'),
)

#Student views: list, create, delete, etc
urlpatterns += patterns('view.student',
    url(r'^students/?$', 'index'),
    url(r'^students/newstudent/(?P<idcourse>\d+)$', 'newstudent'),
    url(r'^students/editstudent/(?P<idcourse>\d+)/(?P<idstudent>\d+)/$', 'editstudent'),
)

urlpatterns += patterns('view.course',
    url(r'^course/?$', 'index'),
    url(r'^course/newcourse/?$', 'newcourse'),
    url(r'^course/editcourse/(?P<idcourse>\d+)$', 'editcourse'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
