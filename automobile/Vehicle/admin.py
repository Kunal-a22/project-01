from django.contrib import admin
from .models.product import product
from.models.category import category
from.models.customer import customer
from.models.order import Order

class Admin_Product(admin.ModelAdmin):
    list_display=("id","Name","Price","category","Description","Image")
# Register your models here.
admin.site.register(product,Admin_Product)


class Admin_Category(admin.ModelAdmin):
    list_display=("Name",)
admin.site.register(category,Admin_Category)

admin.site.register(customer)
admin.site.register(Order)