from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def home(request):
	return HttpResponse("hello world")

def register(request):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
		username = form.cleaned_data.get('username')
		messages.success(request, f'username created for {username}')
		return redirect('user_log_in')
	return render(request, 'users/register.html', {'form' : form})

