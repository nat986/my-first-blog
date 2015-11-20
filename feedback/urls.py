from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.feedback_list, name='feedback_list'),
    url(r'^feedback/(?P<pk>[0-9]+)/$', views.feedback_detail, name='feedback_detail'),
    url(r'^post/new/$', views.feedback_new, name='feedback_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.feedback_edit, name='feedback_edit'),
    url(r'^drafts/$', views.feedback_draft_list, name='feedback_draft_list'),
    url(r'^feedback/(?P<pk>[0-9]+)/publish/$', views.feedback_publish, name='feedback_publish'),
    url(r'^feedback/(?P<pk>[0-9]+)/remove/$', views.feedback_remove, name='feedback_remove'),
]