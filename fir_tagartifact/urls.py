from django.conf.urls import url

from fir_tagartifact import views

urlpatterns = [
    url(r'^(?P<content_type>\d+)/add/(?P<object_id>\d+)$', views.tagartifact_addtag, name='add'),
]
