from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def render_dashboard(request):
    return render(request, 'admin_templates/dashboard.html')