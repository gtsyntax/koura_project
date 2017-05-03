from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['title', 'text', 'status']

class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ['text']