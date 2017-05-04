from rest_framework import generics
from question.models import Question
from .serializers import QuestionModelSerializer
from rest_framework import permissions


class QuestionListAPIView(generics.ListAPIView):
	queryset = Question.objects.all()
	serializer_class = QuestionModelSerializer

class QuestionDetailAPIView(generics.RetrieveAPIView):
	queryset = Question.objects.all()
	serializer_class = QuestionModelSerializer

class QuestionCreateAPIView(generics.CreateAPIView):
	queryset = Question.objects.all()
	serializer_class = QuestionModelSerializer
	permission_classes = [permissions.IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)