from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from ..login.models import User
from .models import Quote, Favorite
import bcrypt, re

# Create your views here.
def index(request):
	all_quotes = Quote.objects.all().order_by('-created_at')
	this_user = User.objects.get(id=request.session['user_id'])
	my_favorites = Favorite.objects.filter(user_id=this_user.id).order_by('-created_at')
	
	my_favorite_quotes = []
	favorites_list = []
	for favorite in my_favorites:
		favorites_list.append(favorite.quote.id)
		my_favorite_quotes.append(favorite.quote)
	
	

	context = {
		'all_quotes': all_quotes,
		'favorites_list': favorites_list,
		'my_favorite_quotes': my_favorite_quotes,
		'my_favorites': my_favorites
	}
	return render(request, 'quotes/index.html', context)

def logout(request):
	request.session.clear()
	messages.success(request,'Logged out successfully')
	return redirect('login:index')

def create_quote(request):
	author = request.POST['txt_author']
	message = request.POST['txt_message']
	this_user = User.objects.get(id=request.session['user_id'])

	if len(author)<1 or len(message)<1:
		messages.warning(request, '*both fields are required to contribute a quote')
		return redirect('quotes:index')
	elif len(author)<4:
		messages.warning(request, 'author must be at least 4 characters long')
		return redirect('quotes:index')
	elif len(message)<11:
		messages.warning(request, 'Message must be more than 10 characters')
		return redirect('quotes:index')
	else:
		new_quote = Quote.objects.create(author=author,message=message,posted_by=this_user)
		this_user.quote_count += 1
		this_user.save()
		messages.success(request, 'New quote created!')
		return redirect('quotes:index')

def show_user(request,user_id):
	this_user = User.objects.get(id=user_id)
	my_quotes = Quote.objects.filter(posted_by=user_id)

	context = {
		'this_user': this_user,
		'my_quotes': my_quotes
	}
	return render(request, 'quotes/show_user.html', context)

def add_to_favorites(request, quote_id):
	this_user = User.objects.get(id=request.session['user_id'])
	this_quote = Quote.objects.get(id=quote_id)

	new_favorite = Favorite.objects.create(user=this_user,quote=this_quote)
	messages.success(request, 'Quote has been favorited!')

	return redirect('quotes:index')

def remove_from_favorites(request,quote_id):
	user_id = request.session['user_id']
	this_quote = Quote.objects.get(id=quote_id)
	this_user = User.objects.get(id=request.session['user_id'])

	
	this_favorite = Favorite.objects.filter(user=user_id,quote=quote_id)
	print 'favorite to delete:',this_favorite[0].id
	this_favorite.delete()

	messages.success(request, 'Quote removed from favorites')

	return redirect('quotes:index')


