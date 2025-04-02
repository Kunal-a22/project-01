from django.shortcuts import render,redirect ,HttpResponseRedirect
from django.contrib.auth.hashers import make_password,check_password
from django.http import HttpResponse
from .models.product import product
from .models import category
from .models import customer
from django.views import View
from django.urls import reverse
from django import template
from .models import Order
from Vehicle.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator
from django.conf import settings

# for testing password
# print(make_password("1234"))
# print(check_password("123456","pbkdf2_sha256$720000$XAloDeEvPHL8igG3R9Ia3o$+eSFlVRb2VFsIwTJoAY3l/rJFf0ynfORwK1Y3PepXJo="))


# Create your views here.
# Class Based View-------------------
class home(View):
    def post(self,request):
        product=request.POST.get("product")
        remove=request.POST.get("remove")
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]=quantity-1
                else:
                    cart[product]=quantity+1
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1
        request.session['cart']=cart
        print(request.session['cart']) 
        return redirect("homepage")
        
    def get(self,request):
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}
        Product=None
        # Product=product.viewAll()
        Category=category.View_All_Category()
        category_id=request.GET.get('category')
        print(category_id)
        if category_id:
            Product=product.view_productByCategoryID(category_id)
        else:
            Product=product.viewAll()
        data={
       
        }
        data['Product']=Product
        data[ 'Category']=Category

        return render(request,"orders/index.html",data)

class Cart(View):
    def get(self, request):
        ids=list(request.session.get('cart').keys())
        products=product.get_product_by_id(ids)
        return render(request,"cart.html",{'products':products}) 


class CheckOut(View):
    def post(self,request):
        print(request.POST)
        
        address=request.POST.get("address")
        phone=request.POST.get("phone")
        cust=request.session.get("id")
        cart=request.session.get('cart')
        print("You are right person",address,phone,customer)
        products=product.get_product_by_id(list(cart.keys()))
        
       
        for product1 in products:
            order=Order(cust=customer(id=cust),
                        pro=product1,
                        price=product1.Price,
                        mobile=phone,
                        qty=cart.get(str(product1.id))
                        )
            order.placeOrder()            
        request.session['cart']={}
       
        return redirect("/orders")

        return redirect("cart")




# Order Page views-----------------------------------

class OrderNow(View):
    
    def get(self,request):
       customer=request.session.get("id")
       print("Hello",customer)
       orders=Order.get_order_by_customer(customer)
        
        
       print("Your orders are",orders)
       return render(request,"orders.html",{'orders':orders})





# Function Based View------------------

# def home(request):
#     Product=None
#     # Product=product.viewAll()
#     Category=category.View_All_Category()
#     category_id=request.GET.get('category')
#     print(category_id)
#     if category_id:
#         Product=product.view_productByCategoryID(category_id)
#     else:
#         Product=product.viewAll()
#     data={
       
#     }
#     data['Product']=Product
#     data[ 'Category']=Category

#     return render(request,"orders/index.html",data)



# signup Register------------------------------------------
def signup(request):
    if request.method=="POST":
        datapost=request.POST
        fname=datapost.get('fname')
        lname=datapost.get('lname')
        phone=datapost.get('phone')
        email=datapost.get('email')
        password=datapost.get('password')       
       

        #maintain dictinary of user entered values
        values={
            'fname':fname,
            'lname':lname,
            'phone':phone,
            'email':email            
        }
       
        c=customer(
            fname=fname,
            lname=lname,
            phone=phone,
            email=email,
            password=password
            )
        #Validation begin now
        error_message=None
        if not fname:
            error_message="First name is Required!!!!"
        elif len(fname)<4:
            error_message="First name must be 4 charecter Long!!!!"
        elif not lname:
            error_message="Last name is Required!!!!"
        elif len(lname)<4:
            error_message="Last name must be 4 charecter Long!!!!"
        elif not phone:
            error_message="Phone Number is Required!!!!!" 
        elif len(phone)<=10:
            error_message="Phone number must be more than 9 Digits!!!!!"   
        elif not password:
            error_message="Password is Required!!!!!" 
        elif len(password)<6:
            error_message="Password must be more than 6 characters Long!!!!!"
        elif len(email)<6:
            error_message="Email Id must be more than 6 charecter Long"
        elif c.is_Exist():
            error_message="Email Id Already Exist"

           
        if not error_message:
            customer1=customer(
            fname=fname,
            lname=lname,
            phone=phone,
            email=email,
            password=password
            )
            customer1.password=make_password(customer1.password)
                
            customer1.register()
            return redirect('homepage')
        else:
            data={
                'error_message':error_message,
                'values':values
            }
            return render(request,"signup.html",data)
    else:
         return render(request,"signup.html")


# Login Page start  
def login(request):
    return_url=None
    if request.method=='POST':
        email=request.POST.get("email")
        password=request.POST.get("password")
        cust=customer.get_customer_byemail(email)
        error_message=None
        if cust:
            flag=check_password(password,cust.password)
            if flag:
                request.session['id']=cust.id
                request.session['email']=cust.email
                print("your customer id is",cust.id)
                print("your email is",cust.email)


                if login.return_url:
                    return HttpResponseRedirect(login.return_url)
                else:
                    login.return_url = None
                    return redirect('homepage')
                

            else:
                error_message="Password is Invalid!!!!"
        else:
            error_message="Email Id is Invalid!!!!"
        return render(request,"login.html",{'error_message':error_message})

    login.return_url =request.GET.get('return_url')
    return render(request,"login.html")



# Logout Page-------------------------------

def logout(request):
    request.session.clear()
    return redirect("login")


# Payment Adding-----------------------------------
def paymentNow(request):
    if request.method=="POST":
        return render(request,'payment.html')





















