from django.conf.urls import url
from . import views

app_name = 'students'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]



