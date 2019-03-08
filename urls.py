from django.conf.urls import patterns, url
from . import views


urlpatterns = [

    url(r'^$', views.course_date, name='course_date'),
    url(r'^$', views.show_data, name='show_data'),


   
]











