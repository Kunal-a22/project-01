from django.db import models
from .product import product
from .customer import customer
import datetime


class Order(models.Model):
    pro=models.ForeignKey(product,on_delete=models.CASCADE)
    cust=models.ForeignKey(customer,on_delete=models.CASCADE)
    qty=models.IntegerField(default=1)
    price=models.IntegerField()
    address=models.CharField(max_length=200, default='',blank=True)
    mobile=models.CharField(max_length=200, default='',blank=True,null=True)
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)
    


    def placeOrder(self):
        self.save()

# include order by date----------------------------        
    @staticmethod
    def get_order_by_customer(customer_id):
        return Order \
            .objects \
            .filter(cust=customer_id)\
            .order_by('-date')
    
    