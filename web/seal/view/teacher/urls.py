from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('view.teacher.home',
    (r'^$', 'index'),
)

urlpatterns += patterns('view.teacher.practice',
    url(r'^practices/?$', 'index'),
    url(r'^practices/newpractice/(?P<idcourse>\d+)$', 'newpractice'),
    url(r'^practices/editpractice/(?P<idcourse>\d+)/(?P<idpractice>\d+)/$', 'editpractice'),
    url(r'^practices/script/(?P<idcourse>\d+)/(?P<idpractice>\d+)/$', 'script'),
    url(r'^practices/practicefile/(?P<idcourse>\d+)/(?P<idpractice>\d+)/$', 'practicefilelist'),
    url(r'^practices/downloadfile/(?P<idpracticefile>\d+)/$', 'download'),
    url(r'^practices/deletefile/(?P<idpracticefile>\d+)/$', 'delete'),
)

urlpatterns += patterns('view.teacher.student',
    url(r'^students/?$', 'index'),
    url(r'^students/newstudent/(?P<idcourse>\d+)$', 'newstudent'),
    url(r'^students/editstudent/(?P<idcourse>\d+)/(?P<idstudent>\d+)/$', 'editstudent'),
    url(r'^students/editstudent/(?P<idstudent>\d+)/$', 'edit_unenrolled_student'),
)

urlpatterns += patterns('view.teacher.course',
    url(r'^course/?$', 'index'),
    url(r'^course/newcourse/?$', 'newcourse'),
    url(r'^course/editcourse/(?P<idcourse>\d+)$', 'editcourse'),
)

urlpatterns += patterns('view.teacher.delivery',
    url(r'^delivery/list/(?P<idpractice>\d+)/$', 'listdelivery'),
    url(r'^delivery/download/(?P<iddelivery>\d+)/$', 'download'),
    url(r'^delivery/browse/(?P<iddelivery>\d+)/(?P<file_to_browse>[\w\-\./]+)/$', 'browse'),
    url(r'^delivery/explore/(?P<iddelivery>\d+)/$', 'explore'),
)

urlpatterns += patterns('view.teacher.correction',
    url(r'^correction/(?P<iddelivery>\d+)/$', 'index'),
    url(r'^correction/edit/(?P<idcorrection>\d+)/$', 'editcorrection'),
)

urlpatterns += patterns('view.teacher.suscription',
    url(r'^suscription/list/(?P<idcourse>\d+)/$', 'listsuscription'),
    url(r'^suscription/acceptGroup/(?P<idcourse>\d+)/', 'acceptgroup'),
    url(r'^suscription/rejectGroup/(?P<idcourse>\d+)/', 'rejectgroup'),
)

urlpatterns += patterns('view.teacher.automatic_correction',
    #url(r'^runautomatic_correction', 'run_automatic_correction_subprocess'),
    url(r'^automatic_correction/(?P<iddelivery>\d+)/$', 'details'),
)
