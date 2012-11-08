from django.conf.urls.defaults import patterns, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


#Student site: home, list assignments, deliver assignment, etc
urlpatterns = patterns('view.undergraduate.home',
    url(r'^$', 'index'),
)

urlpatterns += patterns('view.delivery',
    url(r'^delivery/newdelivery/(?P<idpractice>\d+)/(?P<idstudent>\d+)?/$', 'newdelivery'),
    url(r'^delivery/listdelivery/(?P<idpractice>\d+)/$', 'listdelivery'),
    url(r'^delivery/download/(?P<iddelivery>\d+)/$', 'download'),
)
