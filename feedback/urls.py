from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.feedback_list, name='feedback_list'),
]