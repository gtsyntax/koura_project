from rest_framework import generics
from question.models import Question
from .serializers import QuestionModelSerializer


class QuestionListAPIView(generics.ListAPIView):
	queryset = Question.active.all()
	serializer_class = QuestionModelSerializer

class QuestionDetailAPIView(generics.RetrieveAPIView):
	queryset = Question.active.all()
	serializer_class = QuestionModelSerializer