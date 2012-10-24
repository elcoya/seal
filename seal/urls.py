from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('view.practice',
    url(r'^practice/newpractice', 'newpractice'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
