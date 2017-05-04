from django.utils.timesince import timesince
from rest_framework import serializers
from question.models import Question, Answer
from accounts.api.serializers import UserDisplaySerializer

class QuestionModelSerializer(serializers.ModelSerializer):
	user = UserDisplaySerializer()
	date_display = serializers.SerializerMethodField()
	timesince = serializers.SerializerMethodField()
	class Meta:
		model = Question
		fields = ('title','created','date_display', 'timesince', 'user')

	def get_date_display(self, obj):
		return obj.created.strftime("%b %d")
	def get_timesince(self, obj):
		return timesince(obj.created)

class AnswerModelSerializer(serializers.ModelSerializer):
	user = UserDisplaySerializer()
	class Meta:
		model = Answer
		fields = ('__all__')



