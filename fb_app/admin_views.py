from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from fb_app import models

# Create your views here.
def render_dashboard(request):
    customers = models.Customer.objects.all()
    context = {
        "customers": customers,
    }
    return render(request, 'admin_templates/dashboard.html', context)

def render_customers(request):
    customers = models.Customer.objects.all()
    context = {
        "customers": customers,
    }
    return render(request, 'admin_templates/customers.html', context)

def render_products(request):
    products = models.Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, 'admin_templates/products.html', context)
