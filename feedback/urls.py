from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.feedback_list, name='feedback_list'),
    url(r'^feedback/(?P<pk>[0-9]+)/$', views.feedback_detail, name='feedback_detail'),
]