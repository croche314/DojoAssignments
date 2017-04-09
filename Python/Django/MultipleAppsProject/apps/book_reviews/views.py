from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Book, Review
import bcrypt, re
from django.core.urlresolvers import reverse

# Create your views here.
def start(request):
	return render(request, 'book_reviews/login.html')

def register(request):
	name = request.POST['txt_name']
	alias = request.POST['txt_alias']
	email = request.POST['txt_email']
	password = request.POST['txt_password']
	confirm_pw = request.POST['txt_confirm_pw']

	if len(name)<1 or len(alias)<1 or len(email)<1 or len(password)<1 or len(confirm_pw)<1:
		messages.warning(request,'Please make sure all fields are not blank')
		return redirect('/')
	elif password != confirm_pw:
		messages.warning(request,'passwords must match')
		return redirect('/')
	else:
		new_user = User.objects.create(name=name,alias=alias,email=email,password=password)
		request.session['user_id'] = new_user.id
		request.session['alias'] = new_user.alias
		request.session['email'] = new_user.email
		messages.success(request,'New user created! Welcome!')
		return redirect('/books')


def login(request):
	email = request.POST['txt_email']
	password = request.POST['txt_password']

	this_user = User.objects.get(email=email)
	if this_user.password == password:
		request.session['user_id'] = this_user.id
		request.session['alias'] = this_user.alias
		request.session['email'] = this_user.email
		return redirect('/books')
	else:
		messages.warning(request,'invalid login')
		return redirect('/')

def logout(request):
	request.session.flush()
	messages.success(request,'Logged out successfully')
	return redirect('/')


def index(request):
	all_books = Book.objects.all()
	all_reviews = Review.objects.all()
	recent_reviews = Review.objects.all().order_by('-created_at')[:3]
	book_list = []
	for review in recent_reviews:
		book_list.append(review.book_id)

	not_recent_reviews = Review.objects.all()[3:]
	not_recent_books = []

	for review in not_recent_reviews:
		not_recent_books.append(review.book)

	not_recent_set = set(not_recent_books)

	context = {
		'recent_reviews': recent_reviews,
		'not_recent_reviews': not_recent_reviews,
		'book_list': book_list,
		'not_recent_set': not_recent_set
	}
	return render(request, 'book_reviews/index.html', context)

def new_book(request):
	return render(request, 'book_reviews/new_book.html')

def create_book(request):
	if len(request.POST['select_author']) > 0:
		author = request.POST['select_author']
	else:
		author = request.POST['txt_author']
	review_text = request.POST['review_text']
	rating = request.POST['stars']
	this_user = User.objects.get(id=request.session['user_id'])
	this_book = Book.objects.filter(title=request.POST['txt_book_title'])
	if len(this_book) > 0:
		print 'already have book!'
		this_book = Book.objects.get(title=request.POST['txt_book_title'])
		title = request.POST['txt_book_title']
		new_review = Review.objects.create(user=this_user,book=this_book,rating=rating,review_text=review_text)
	else:
		print 'new book!'
		title = request.POST['txt_book_title']
		new_book = Book.objects.create(title=title,author=author)
		new_review = Review.objects.create(user=this_user,book=new_book,rating=rating,review_text=review_text)
	
	messages.success(request,'New Book and Review Added!')
	return redirect('/books')

def show_book(request, book_id):
	this_book = Book.objects.get(id=book_id)
	print 'book:',this_book.title
	all_my_reviews = Review.objects.filter(book=book_id).order_by('-created_at')

	context = {
		'this_book': this_book,
		'all_my_reviews': all_my_reviews
	}

	return render(request, 'book_reviews/show_book.html', context)

def add_review(request,book_id):
	this_book = Book.objects.get(id=book_id)
	this_user = User.objects.get(id=request.session['user_id'])
	rating = request.POST['stars']
	review_text = request.POST['review_text']

	new_review = Review.objects.create(user=this_user,book=this_book,rating=rating,review_text=review_text)

	return redirect('/books/'+book_id)

def destroy_review(request,review_id):
	this_review = Review.objects.get(id=review_id)
	book_id = this_review.book.id
	this_review.delete()

	messages.success(request,'review deleted')
	return redirect('/books/'+str(book_id))

def show_user(request,user_id):
	this_user = User.objects.get(id=user_id)
	my_reviews = Review.objects.filter(user_id=user_id)

	my_reviewed_books = []
	for review in my_reviews:
		my_reviewed_books.append(review.book)

	print 'my_reviewed_books:',set(my_reviewed_books)
	
	context = {
		'this_user': this_user,
		'my_reviewed_books': set(my_reviewed_books)
	}

	return render(request, 'book_reviews/show_user.html', context)


