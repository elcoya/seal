from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Index page. DO NOT TOUCH
urlpatterns = patterns('django.views.generic.simple',
    (r'^$', 'direct_to_template', {'template': 'index.html'}),
)

urlpatterns += patterns('view.practice',
    url(r'^practice/?$', 'index'),
    url(r'^practice/newpractice/?$', 'newpractice'),
)

#Student views: list, create, delete, etc
urlpatterns += patterns('view.student',
    url(r'^students/?$', 'index'),
    url(r'^students/newstudent/?$', 'newstudent'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
