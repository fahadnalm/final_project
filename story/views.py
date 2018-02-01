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
	page = Page.objects.get(id=1) #starting page
	context = {
		'page': page,
	}

	return render(request, 'start.html', context)

def next_page(request, option_id):
	option = Option.objects.get(id=option_id)
	 #Page.objects.get(option_id=) #Is this A or B or C?  Retrieve the user option 

	next_page = option.nextpage #Extract the next page of that choice
	context = {
		'page': next_page
	}
	return render(request, 'start.html', context)
