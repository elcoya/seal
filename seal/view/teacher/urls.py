from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('view.teacher.home',
    (r'^$', 'index'),
)

urlpatterns += patterns('view.practice',
    url(r'^practices/?$', 'index'),
    url(r'^practices/newpractice/(?P<idcourse>\d+)$', 'newpractice'),
    url(r'^practices/editpractice/(?P<idcourse>\d+)/(?P<idpractice>\d+)/$', 'editpractice'),
    url(r'^practices/download/(?P<idpractice>\d+)/$', 'download')
)

urlpatterns += patterns('view.student',
    url(r'^students/?$', 'index'),
    url(r'^students/newstudent/(?P<idcourse>\d+)$', 'newstudent'),
    url(r'^students/editstudent/(?P<idcourse>\d+)/(?P<idstudent>\d+)/$', 'editstudent'),
    url(r'^students/editstudent/(?P<idstudent>\d+)/$', 'edit_unenrolled_student'),
)

urlpatterns += patterns('view.course',
    url(r'^course/?$', 'index'),
    url(r'^course/newcourse/?$', 'newcourse'),
    url(r'^course/editcourse/(?P<idcourse>\d+)$', 'editcourse'),
)

urlpatterns += patterns('view.teacher.delivery',
    url(r'^delivery/list/(?P<idpractice>\d+)/$', 'listdelivery'),
    url(r'^delivery/download/(?P<iddelivery>\d+)/$', 'download'),
)

urlpatterns += patterns('view.teacher.correction',
    url(r'^correction/(?P<iddelivery>\d+)/$', 'index'),
    url(r'^correction/edit/(?P<idcorrection>\d+)/$', 'editcorrection'),
)

urlpatterns += patterns('view.teacher.suscription',
    url(r'^suscription/list/(?P<idcourse>\d+)/$', 'listsuscription'),
    url(r'^suscription/accept/(?P<idsuscription>\d+)/$', 'accept'),
    url(r'^suscription/reject/(?P<idsuscription>\d+)/$', 'reject'),
    url(r'^suscription/acceptGroup/(?P<idcourse>\d+)/', 'acceptGroup'),
    url(r'^suscription/rejectGroup/(?P<idcourse>\d+)/', 'rejectGroup'),
)
