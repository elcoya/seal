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
    url(r'^practices/newpractice/?$', 'newpractice'),
)

#Student views: list, create, delete, etc
urlpatterns += patterns('view.student',
    url(r'^students/?$', 'index'),
    url(r'^students/newstudent/?$', 'newstudent'),
)

urlpatterns += patterns('view.course',
    url(r'^course/?$', 'index'),
    url(r'^course/newcourse/?$', 'newcourse'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
