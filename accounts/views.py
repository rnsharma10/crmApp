from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *


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
