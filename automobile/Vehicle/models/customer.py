from django.db import models

class customer(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    password=models.CharField(max_length=500)

    def register(self):
        self.save()
        

    def get_customer_byemail(email):
        try:
            return customer.objects.get(email=email)
        except:
            return False
        

    def is_Exist(self):
        if customer.objects.filter(email=self.email):
            return True
        else:
            return False

