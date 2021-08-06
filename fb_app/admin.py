from django.contrib import admin
from fb_app import models

# Register your models here.
admin.site.register(models.Customer)
admin.site.register(models.Product)
admin.site.register(models.Session)
admin.site.register(models.Schedule)
admin.site.register(models.Sale)
admin.site.register(models.Expense)
admin.site.register(models.Payment)