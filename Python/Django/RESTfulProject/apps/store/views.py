from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Product,ExampleModel

from .forms import ImageUploadForm


def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        
    return HttpResponse('image upload success')
    
# Create your views here.
def index(request):
	query = Product.objects.all()
	context = {
		'all_products': query
	}
	return render(request, 'store/index.html', context)

def new(request):
	return render(request, 'store/new_product.html')

def create(request):
	this_name = request.POST['txt_name']
	this_description = request.POST['txt_description']
	this_price = request.POST['txt_price']

	Product.objects.create(name=this_name,description=this_description,price=this_price)
	messages.success(request,'New product added!')
	return redirect('/')

def show(request,id):
	this_product = Product.objects.get(id=id)
	context = {
		'product': this_product
	}

	return render(request, 'store/show_product.html', context)

def edit(request,id):
	this_product = Product.objects.get(id=id)
	context = {
		'product': this_product
	}

	return render(request, 'store/edit_product.html', context)

def update(request,id):
	this_name = request.POST['txt_name']
	this_description = request.POST['txt_description']
	this_price = request.POST['txt_price']

	Product.objects.filter(id=id).update(name=this_name,description=this_description,price=this_price)
	messages.success(request,'Product updated!')

	return redirect('/')

def destroy(request,id):
	this_product = Product.objects.get(id=id)
	this_product.delete()

	messages.success(request,'Product deleted!')
	return redirect('/')
