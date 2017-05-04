from django.conf.urls import url
from .views import (
		QuestionListAPIView,
		QuestionDetailAPIView,
		QuestionCreateAPIView
	)

urlpatterns = [
	url(r'^question/$', QuestionListAPIView.as_view(), name='question_list'),
	# url(r'^question/(?P<slug>[-\w]+)/$', QuestionDetailAPIView.as_view(), name='question_detail'),
	url(r'^question/create/$', QuestionCreateAPIView.as_view(), name='question_create'),
	
]