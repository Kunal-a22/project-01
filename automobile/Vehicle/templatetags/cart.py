from django import template


register=template.Library()
@register.filter(name="is_in_cart")
def is_in_cart(product,cart):
    keys=cart.keys()
    for id in keys:
        if int(id)==product.id:
            return True
        
    # print(product,cart)
    return False

# Quantity Filter-----------
@register.filter(name="cart_qty")
def cart_qty(product,cart):
    keys=cart.keys()
    for id in keys:
        if int(id)==product.id:
            return cart.get(id)
    
    return 0


# Quantity add 
@register.filter(name="price_total")
def price_total(product,cart):
    return product.Price*cart_qty(product,cart)

# filter for grand total
@register.filter(name="grand_total")
def grand_total(products,cart):
    sum=0
    for p in products:
        sum+=price_total(p,cart)
    return sum


# for currency sign filter
@register.filter(name="currency")
def currency(number):
    return " ₹ "+str(number)


@register.filter(name="multiply")
def multiply(number,number1):
    return number*number1