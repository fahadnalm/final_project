from django.shortcuts import render
from django.http import HttpResponse
from story.models import Story, Page, Option
from .forms import PageForm

def home(request):
	context = {}
	return render(request, 'home.html', context)

def about_game(request):
	context = {}
	return render(request, 'about_game.html', context)

def start(request):
	page = Page.objects.get(id=1) #starting page
	form = PageForm(request.POST or None, request.FILES or None)
	context = {
		'page': page,
	}

	return render(request, 'start.html', context)

def next_page(request, option_id):
	option = Option.objects.get(id=option_id)
	form = PageForm(request.POST or None, request.FILES or None)
	next_page = option.nextpage #Extract the next page of that choice

	if len(next_page.current_page.all()) == 0:
		context = {
		'gameover': next_page.text,
		'reason': next_page.reason,
		'img': next_page.image
		}
		return render(request, 'gameover.html', context)

	 #Page.objects.get(option_id=) #Is this A or B or C?  Retrieve the user option 

	context = {
		'page': next_page,
	}
	return render(request, 'start.html', context)
