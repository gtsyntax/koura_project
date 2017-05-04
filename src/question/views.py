from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Question, Answer 
from .forms import QuestionForm, AnswerForm

# Code for handling question views

def question_list(request):
	# qs = Question.objects.filter(status="published")
	qs = Question.objects.all()
	question_form = QuestionForm(request.POST or None)
	if question_form.is_valid():
		new_question = question_form.save(commit=False)
		new_question.user = request.user
		new_question.save()
	template = 'question/list.html'
	context = {
		"questions": qs,
		"question_form": question_form
	}
	return render(request, template, context)

def question_detail(request, id=None):
	question = get_object_or_404(Question, id=id)
	answers = question.answers.filter(active=True)
	answer_form = AnswerForm(request.POST or None)
	if answer_form.is_valid():
		new_answer = answer_form.save(commit=False)
		# Assign the new answer to the question object specified above.
		new_answer.question =  question
		# Assign the current answer to the active user to avoid integrity error.
		new_answer.user = request.user
		# Save to database.
		new_answer.save()

	template = 'question/detail.html'
	context = {
		"question": question,
		"answer_form": answer_form,
		"answers": answers
	}
	return render(request, template, context)

@login_required
def question_create(request):
	form = QuestionForm(request.POST or None)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.user = request.user
		obj.save()
		messages.success(request, "Created New Question")
		return HttpResponseRedirect('/question/{num}'.format(num=obj.id))
	template = 'question/create.html'
	context = {
		"form": form
	}
	return render(request, template, context)
@login_required
def question_update(request, id=None):
	obj = get_object_or_404(Question, id=id)
	form = QuestionForm(request.POST or None, instance=obj)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.save()
		messages.success(request, "Updated Question")
		return HttpResponseRedirect('/question/{num}'.format(num=obj.id))
	template = 'question/update.html'
	context = {
		"form": form
	}
	return render(request, template, context)

@login_required
def question_delete(request, id=None):
	obj = get_object_or_404(Question, id=id)
	if request.method == 'POST':
		obj.delete()
		messages.success(request, "Post deleted")
		return HttpResponseRedirect('/question/')
	template = 'question/delete.html'
	context = {
		"question": obj
	}
	return render(request, template, context)





