from django.conf.urls import include, url
from .views import (
		question_list,
		question_detail,
		question_create,
		question_update,
		question_delete
	)

urlpatterns = [
    url(r'^$', question_list, name="list"),
    url(r'^create/', question_create, name="create"),
    url(r'^(?P<slug>[-\w]+)/$', question_detail, name="detail"),
    url(r'^(?P<slug>[-\w]+)/edit/$', question_update, name="update"),
    url(r'^(?P<slug>[-\w]+)/delete/$', question_delete, name="delete"),
]