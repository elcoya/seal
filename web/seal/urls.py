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
