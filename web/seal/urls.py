from django.conf.urls.defaults import patterns, include, url
#import serializer
from rest_framework.urlpatterns import format_suffix_patterns
from seal.view import serializer

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
    url(r'^changepassw/?$', home.change_password),
    url(r'^login/?$', 'django.contrib.auth.views.login'),
    url(r'^recoverypass/?$', home.recovery_pass),
    url(r'^changelenguaje/?$', home.change_lenguaje),
    url(r'^i18n/', include('django.conf.urls.i18n'))
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^teacher/?', include('view.teacher.urls')),
)

urlpatterns += patterns('',
    url(r'^undergraduate/?', include('view.undergraduate.urls')),
)

#url serializer
urlpatterns += patterns('',
    url(r'^mailserializer/$', serializer.MailList.as_view(), name='mail-list'),
    url(r'^mailserializer/(?P<pk>\d+)/?$', serializer.MailDetail.as_view(), name='mail-detail'),
)

# Format suffixes
urlpatterns += format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

# Default login/logout views
urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)