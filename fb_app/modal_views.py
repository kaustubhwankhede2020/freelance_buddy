from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from fb_app import models


# Create your views here.

# View to Add Customers
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
        customer_obj = models.Customer(first_name=first_name, last_name=last_name, age=age, email=email, gender=gender,
                                       mobile_no_1=mobile_no_1, mobile_no_2=mobile_no_2, mobile_no_3=mobile_no_3,
                                       city=city, state=state, country=country, address=address, profession=profession,
                                       customer_source=customer_source, description=description,
                                       additional_notes=additional_notes, bank_details=bank_details,
                                       time_zone=time_zone)
        customer_obj.save()
        messages.success(request, "Customer Registration Sucessful")
        return HttpResponseRedirect(reverse("render_dashboard"))


# View to add new Products
def perform_add_product(request):
    if request.method != 'POST':
        return HttpResponse("Method not Allowed")
    else:
        product_title = request.POST.get('product_title')
        product_description = request.POST.get('product_description')
        listing_unit_price = request.POST.get('listing_unit_price')
        product_obj = models.Product(product_title=product_title, product_description=product_description,
                                     listing_unit_price=listing_unit_price)
        product_obj.save()
        messages.success(request, "Product Registration Successful")
        return HttpResponseRedirect(reverse("render_dashboard"))


def perform_add_session(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed")
    else:
        session_title = request.POST.get("session_title")
        session_description = request.POST.get("session_description")
        date = request.POST.get("date")
        time = request.POST.get("time")
        location = request.POST.get("location")
        notes = request.POST.get("notes")
        duration = request.POST.get("duration")
        repeat = request.POST.get("repeat")
        session_obj = models.Session(session_title=session_title, session_description=session_description, date=date,
                                     time=time, location=location, notes=notes, duration=duration, repeat=repeat)
        session_obj.save()
        messages.success(request, "Session Registration Successful")
        return HttpResponseRedirect(reverse("render_dashboard"))


def perform_add_schedule(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed")
    else:
        date = request.POST.get("date")
        time = request.POST.get("time")
        location = request.POST.get("location")
        notes = request.POST.get("notes")
        customer_id = request.POST.get("customer_id")
        product_id = request.POST.get("product_id")
        session_id = request.POST.get("session_id")
        status = request.POST.get("status")
        customer = models.Customer.objects.get(main_id=customer_id)
        product = models.Product.objects.get(main_id=product_id)
        session = models.Session.objects.get(main_id=session_id)
        schedule_obj = models.Schedule(date=date, time=time, location=location, notes=notes, customer_id=customer,
                                       product_id=product, session_id=session, status=status)
        schedule_obj.save()
        messages.success(request, "Schedule Registration Successful")
        return HttpResponseRedirect(reverse("render_dashboard"))


def perform_add_sale(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed")
    else:
        sale_title = request.POST.get("sale_title")
        sale_description = request.POST.get("sale_description")
        sale_price = request.POST.get("sale_price")
        package_maturity = request.POST.get("package_maturity")
        no_of_sessions = request.POST.get("no_of_sessions")
        session_frequency = request.POST.get("session_frequency")
        session_frequency_unit = request.POST.get("session_frequency_unit")
        customer_id = request.POST.get("customer_id")
        product_id = request.POST.get("product_id")
        customer = models.Customer.objects.get(main_id=customer_id)
        product = models.Product.objects.get(main_id=product_id)
        sale_obj = models.Sale(sale_title=sale_title, sale_description=sale_description, sale_price=sale_price,
                               package_maturity=package_maturity, no_of_sessions=no_of_sessions,
                               session_frequency=session_frequency, session_frequency_unit=session_frequency_unit,
                               customer_id=customer, product_id=product)
        sale_obj.save()
        messages.success(request, "Sale Registration Successful")
        return HttpResponseRedirect(reverse("render_dashboard"))


def perform_add_payment(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed")
    else:
        payment_title = request.POST.get("payment_title")
        payment_description = request.POST.get("payment_description")
        payment_amount = request.POST.get("payment_amount")
        payment_method = request.POST.get("payment_method")
        currency = request.POST.get("currency")
        customer_id = request.POST.get("customer_id")
        sale_id = request.POST.get("sale_id")
        customer = models.Customer.objects.get(main_id=customer_id)
        sale = models.Sale.objects.get(main_id=sale_id)
        payment_obj = models.Payment(payment_title=payment_title, payment_description=payment_description,
                                     payment_amount=payment_amount, payment_method=payment_method, currency=currency,
                                     customer_id=customer, sale_id=sale)
        payment_obj.save()
        messages.success(request, "Payment Registration Successful")
        return HttpResponseRedirect(reverse("render_dashboard"))


def perform_add_expense(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed")
    else:
        expense_title = request.POST.get("expense_title")
        expense_description = request.POST.get("expense_description")
        expense_amount = request.POST.get("expense_amount")
        expense_allocation_flag = request.POST.get("expense_allocation_flag")
        expense_type = request.POST.get("expense_type")
        package_id = request.POST.get("package_id")
        customer_id = request.POST.get("customer_id")
        customer = models.Customer.objects.get(main_id=customer_id)
        expense_obj = models.Expense(expense_title=expense_title, expense_description=expense_description,
                                     expense_amount=expense_amount, expense_allocation_flag=expense_allocation_flag,
                                     expense_type=expense_type, package_id=package_id, customer_id=customer)
        expense_obj.save()
        messages.success(request, "Expense Registration Successful")
        return HttpResponseRedirect(reverse("render_dashboard"))
