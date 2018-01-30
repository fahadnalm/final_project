from django.shortcuts import render
from django.http import HttpResponse
from story.models import Story, Page, Option

def home(request):
	context = {}
	return render(request, 'home.html', context)

def about_game(request):
	context = {}
	return render(request, 'about_game.html', context)

def start(request):
	options = Option.objects.all()
	context = {'options':options}
	return render(request, 'start.html', context)

def next_page(request, user_choice, next_page):
	option = Option.objects.get(choice=user_choice) #Is this A or B or C?  Retrieve the user option 

	next_page = option.nextpage #Extract the next page of that choice
	context = {'option':option}
	return render(request, 'next_page.html', context)
