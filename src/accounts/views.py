from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.
@login_required
def dashboard(request):
	template = 'accounts/dashboard.html'
	context = {
		'section': 'dashboard'
	}
	return render(request, template, context)

# def user_login(request):
# 	login_form = LoginForm(request.POST)
# 	if login_form.is_valid():
# 		form_clean = login_form.cleaned_data
# 		user = authenticate(
# 				username=form_clean['username'],
# 				password=form_clean['password']
# 			)
# 		if user is not None:
# 			if user.is_active:
# 				login(request, user)
# 				return HttpResponse('Authenticated successfully')
# 			else:
# 				return HttpResponse('Disabled account')
# 		else:
# 			return HttpResponse('Invalid login')
# 	else:
# 		login_form = LoginForm()
# 	template = 'accounts/login.html'
# 	context = {
# 		"login_form": login_form 
# 	}
# 	return render(request, template, context)
