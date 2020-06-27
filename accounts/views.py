from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import *
from .forms import OrderForm

def home(request):
	orders = order.objects.all()
	customers = Customer.objects.all()
	total_customers = customers.count()
	total_orders = order.objects.all().count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()

	context = {
		'orders': orders,
		'customers': customers,
		'total_customers': total_customers,
		'total_orders': total_orders,
		'delivered': delivered,
		'pending': pending
	}

	return render(request,'accounts/dashboard.html', context)

def customer(request, pk):
	customer = Customer.objects.get(id=pk)
	orders = customer.order_set.all()
	order_count = orders.count()
	context={
		'customer':customer,
		'order': orders,
		'order_count':order_count
	}
	return render(request,'accounts/customer.html', context)

def products(request):
	products = Product.objects.all();
	return render(request,'accounts/products.html',{'products': products})

def createOrder(request):
	form = OrderForm()
	if request.method=='POST':
		#print('printing post', request.POST)
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context={
		'form':form
	}
	return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):
	ord = order.objects.get(id=pk)
	form = OrderForm(instance=ord)
	
	if request.method=='POST':
		#print('printing post', request.POST)
		form = OrderForm(request.POST, instance=ord)
		if form.is_valid():
			form.save()
			return redirect('/')
	context={
		'form':form
	}
	return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):
	ord = order.objects.get(id=pk)
	
	
	if request.method=='POST':
		#print('printing post', request.POST)
		ord.delete()
		return redirect('/')
		
	context={
		'order': ord,
		'customer':ord.customer.name
	}
	return render(request, 'accounts/delete.html', context)