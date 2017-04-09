from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .. login.models import User
from .models import Recipe
import bcrypt, re

# Create your views here.
def index(request):
	return render(request, 'recipes_app/index.html')

def logout(request):
	request.session.clear()
	return redirect('login:index')

def new_recipe(request):
	return render(request, 'recipes_app/new_recipe.html')

def create_recipe(request):
	this_user = User.objects.get(id=request.session['user_id'])
	title = request.POST['txt_title']
	make_time = request.POST['txt_make_time']
	recipe_text = request.POST['recipe_text']
	image_url = request.POST['txt_image_url']
	
	if len(title)<1 or len(make_time)<1 or len(recipe_text)<1 or len(image_url)<1:
		messages.success(request, 'Please fill out all fields')
		return redirect('recipes:new_recipe')
	else:
		new_recipe = Recipe.objects.create(user=this_user,recipe_title=title,recipe_make_time=make_time,recipe_text=recipe_text, image_url=image_url)
	return redirect('recipes:index')