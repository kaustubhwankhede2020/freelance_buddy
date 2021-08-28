from django.db import models


# Create your models here.
class Customer(models.Model):
    main_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.CharField(max_length=4)
    email = models.EmailField()
    gender = models.CharField(max_length=10, default="")
    mobile_no_1 = models.CharField(max_length=15)
    mobile_no_2 = models.CharField(max_length=15)
    mobile_no_3 = models.CharField(max_length=15)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    address = models.TextField()
    profession = models.CharField(max_length=30)
    customer_source = models.CharField(max_length=30)
    description = models.TextField()
    additional_notes = models.TextField()
    bank_details = models.TextField()
    time_zone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Product(models.Model):
    main_id = models.AutoField(primary_key=True)
    product_title = models.CharField(max_length=50)
    product_description = models.TextField()
    listing_unit_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_title


class Session(models.Model):
    main_id = models.AutoField(primary_key=True)
    session_title = models.CharField(max_length=50)
    session_description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.TextField()
    notes = models.TextField()
    duration = models.TextField(max_length=10)
    repeat = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.session_title


class Schedule(models.Model):
    main_id = models.AutoField(primary_key=True)
    date = models.DateField()
    time = models.TimeField()
    location = models.TextField()
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, default=True)
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, default=True)
    session_id = models.ForeignKey(Session, on_delete=models.DO_NOTHING, default=True)
    status = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.session_id} {self.date} {self.time}'


class Sale(models.Model):
    main_id = models.AutoField(primary_key=True)
    sale_title = models.CharField(max_length=50)
    sale_description = models.TextField()
    sale_price = models.FloatField()
    package_maturity = models.CharField(max_length=20)
    no_of_sessions = models.FloatField()
    session_frequency = models.CharField(max_length=50)
    session_frequency_unit = models.CharField(max_length=40)
    customer_id = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, default=True)
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sale_title


class Expense(models.Model):
    main_id = models.AutoField(primary_key=True)
    expense_title = models.CharField(max_length=50)
    expense_description = models.TextField()
    expense_amount = models.IntegerField()
    expense_allocation_flag = models.CharField(max_length=50)
    expense_type = models.CharField(max_length=40)
    package_id = models.CharField(max_length=50)
    customer_id = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.expense_title


class Payment(models.Model):
    main_id = models.AutoField(primary_key=True)
    payment_title = models.CharField(max_length=50)
    payment_description = models.TextField()
    payment_amount = models.FloatField()
    payment_method = models.CharField(max_length=40)
    currency = models.CharField(max_length=10)
    customer_id = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, default=True)
    sale_id = models.ForeignKey(Sale, on_delete=models.DO_NOTHING, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_title


