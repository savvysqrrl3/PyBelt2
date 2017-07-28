from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^pokes$', views.index),
    url(r'^logout$', views.logout),
    url(r'^givePoke/(?P<id>\d+)$', views.givePoke),
]