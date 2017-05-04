from django.conf.urls import url
from .views import (
		QuestionListAPIView,
		QuestionDetailAPIView
	)

urlpatterns = [
	url(r'^question/$', QuestionListAPIView.as_view(), name='question_list'),
	url(r'^question/(?P<pk>\d+)/$', QuestionDetailAPIView.as_view(), name='question_detail'),
	
]