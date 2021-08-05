from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def test(request):
    return HttpResponse("Hello, World")

def render_login(request):
    return render(request, "auth_templates/login.html")

def perform_login(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed")
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('render_dashboard'))
        else:
            messages.error(request, 'Invalid Credentials')
            return HttpResponseRedirect("/")

def perform_logout(request):
    logout(request)
    return HttpResponseRedirect("/")

def render_dashboard(request):
    return HttpResponse("Admin Home")