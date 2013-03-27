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
    url(r'^practices/editfile/(?P<idpracticefile>\d+)/$', 'edit'),
    url(r'^practices/deletepractice/(?P<idpractice>\d+)/$', 'deletepractice'),

)

urlpatterns += patterns('view.teacher.student',
    url(r'^students/?$', 'index'),
    url(r'^students/pendingdelivery/$', 'pendingdeliveries'),
    url(r'^students/newstudent/(?P<idshift>\d+)$', 'newstudent'),
    url(r'^students/editstudent/(?P<idshift>\d+)/(?P<idstudent>\d+)/$', 'editstudent'),
    url(r'^students/editstudent/(?P<idstudent>\d+)/$', 'edit_unenrolled_student'),
    url(r'^students/list/(?P<idshift>\d+)/$', 'list_student'),
    url(r'^students/listdeliveries/(?P<idstudent>\d+)/$', 'list_student_deliveries'),
    url(r'^students/search/$', 'studentsearch'),
    url(r'^students/detail/(?P<idstudent>\d+)/$', 'studentdetail'),
)

urlpatterns += patterns('view.teacher.shift',
    url(r'^shifts/newshift/(?P<idcourse>\d+)/?$', 'newshift'),
    url(r'^shifts/editshift/(?P<idshift>\d+)/?$', 'editshift'),
    url(r'^shifts/deleteshift/(?P<idshift>\d+)/?$', 'deleteshift'),
)

urlpatterns += patterns('view.teacher.course',
    url(r'^course/?$', 'index'),
    url(r'^course/newcourse/?$', 'newcourse'),
    url(r'^course/editcourse/(?P<idcourse>\d+)$', 'editcourse'),
    url(r'^course/detailcourse/(?P<idcourse>\d+)$', 'detailcourse'),
)

urlpatterns += patterns('view.teacher.delivery',
    url(r'^delivery/list/(?P<idpractice>\d+)/$', 'listdelivery'),
    url(r'^delivery/download/(?P<iddelivery>\d+)/$', 'download'),
    url(r'^delivery/browse/(?P<iddelivery>\d+)/(?P<file_to_browse>[\w\-\./]+)/$', 'browse'),
    url(r'^delivery/explore/(?P<iddelivery>\d+)/$', 'explore'),
    url(r'^delivery/detail/(?P<iddelivery>\d+)/$', 'detail'),
)

urlpatterns += patterns('view.teacher.correction',
    url(r'^correction/(?P<iddelivery>\d+)/(?P<previus>\d+)/$', 'index'),
    url(r'^correction/edit/(?P<idcorrection>\d+)/(?P<previus>\d+)/$', 'editcorrection'),
)

urlpatterns += patterns('view.teacher.suscription',
    url(r'^suscription/list/(?P<idshift>\d+)/$', 'listsuscription'),
    url(r'^suscription/acceptGroup/(?P<idshift>\d+)/', 'acceptgroup'),
    url(r'^suscription/rejectGroup/(?P<idshift>\d+)/', 'rejectgroup'),
    url(r'^suscription/listsuscriptionpending/', 'listsuscriptionpending'),
)

urlpatterns += patterns('view.teacher.automatic_correction',
    #url(r'^runautomatic_correction', 'run_automatic_correction_subprocess'),
    url(r'^automatic_correction/(?P<iddelivery>\d+)/$', 'details'),
)

urlpatterns += patterns('view.teacher.export',
    url(r'^export/$', 'choose'),
    url(r'^export/download/(?P<idcourse>\d+)/$', 'download'),
)

