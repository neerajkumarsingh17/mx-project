from django.conf.urls import patterns, url
from . import views


urlpatterns = [
    
    url(r'^enroll_user/', views.enroll_user, name='enroll_user'),
    url(r'^check_status/', views.check_status, name='check_status'),
]
