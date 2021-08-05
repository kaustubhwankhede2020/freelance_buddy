from django.db import models

# Create your models here.
class Customer(models.Model):
    main_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.CharField(max_length=4)
    email = models.EmailField()
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
