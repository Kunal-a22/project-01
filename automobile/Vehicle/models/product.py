from django.db import models
from .category import category


# Create your models here.
class product(models.Model):
    Name=models.CharField(max_length=50)
    Price=models.IntegerField(default=0)
    category=models.ForeignKey(category,on_delete=models.CASCADE,default="")
    Description=models.CharField(max_length=200,default="")
    Image=models.ImageField(upload_to="media/products/")

    @staticmethod
    def viewAll():
        return product.objects.all()
    @staticmethod
    def view_productByCategoryID(category_id):
        if category_id:
            return product.objects.filter(category=category_id)
        else:
            return product.viewAll()

    
    # cart list     
    @staticmethod
    def get_product_by_id(ids):
        return product.objects.filter(id__in=ids)