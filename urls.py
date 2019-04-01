from django.conf.urls import patterns, url
from . import views


urlpatterns = [

    url(r'^$', views.course_date, name='course_date'),
    url(r'^enroll_user/', views.enroll_user, name='enroll_user'),
    url(r'^check_status/', views.check_status, name='check_status'),
    # url(r'^(?P<task_id>[\w-]+)/$', views.get_progress, name='task_status')
]
