from django.conf.urls.defaults import patterns, url

#Student site: home, list assignments, deliver assignment, etc
urlpatterns = patterns('view.undergraduate.home',
    url(r'^$', 'index'),
)

urlpatterns += patterns('view.undergraduate.practice',
    url(r'^practice/list/(?P<idcourse>\d+)/$', 'practicelist'),
    url(r'^practice/download/(?P<idpractice>\d+)/$', 'download'),
)

urlpatterns += patterns('view.undergraduate.delivery',
    url(r'^delivery/upload/(?P<idpractice>\d+)/$', 'newdelivery'),
)

urlpatterns += patterns('view.undergraduate.correction',
    url(r'^correction/consult/(?P<iddelivery>\d+)/$', 'consultcorrection'),
)
