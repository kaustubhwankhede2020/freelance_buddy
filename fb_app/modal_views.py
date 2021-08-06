from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from fb_app import models

# Create your views here.
def perform_add_customer(request):
    if request.method != 'POST':
        return HttpResponse("Method not Allowed")
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        mobile_no_1 = request.POST.get('mobile_no_1')
        mobile_no_2 = request.POST.get('mobile_no_2')
        mobile_no_3 = request.POST.get('mobile_no_3')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        address = request.POST.get('address')
        profession = request.POST.get('profession')
        customer_source = request.POST.get('customer_source')
        description = request.POST.get('description')
        additional_notes = request.POST.get('additional_notes')
        bank_details = request.POST.get('bank_details')
        time_zone = request.POST.get('time_zone')
        customer_obj = models.Customer(first_name=first_name, last_name=last_name, age=age, email=email, gender=gender, mobile_no_1=mobile_no_1, mobile_no_2=mobile_no_2, mobile_no_3=mobile_no_3, city=city, state=state, country=country, address=address, profession=profession, customer_source=customer_source, description=description, additional_notes=additional_notes, bank_details=bank_details, time_zone=time_zone)
        customer_obj.save()
        messages.success(request, "Customer Registration Sucessful")
        return HttpResponseRedirect(reverse("render_dashboard"))