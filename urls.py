from django.conf.urls import patterns, url
from . import views


urlpatterns = [

    url(r'^$', views.course_date, name='course_date'),
    url(r'^enrolled_data/', views.enrolled_data, name='enrolled_data'),


   
]











