from django.db import models
from products.models import Product,Variation
# Create your models here.

class CartItem(models.Model):
    cart = models.ForeignKey('Cart',on_delete=models.CASCADE,null = True,blank = True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null = True,blank = True)
    variations = models.ManyToManyField(Variation,null = True,blank = True)
    line_total = models.DecimalField(decimal_places=2,max_digits=100,default = 20.00)
    quantity = models.IntegerField(default=1)
    notes = models.TextField(null=True,blank=True)


    def __str__(self):
        try:
            return str(self.cart.id)
        except:
            return self.product.title



class Cart(models.Model):
    # items = models.ManyToManyField(CartItem,null = True,blank = True)
    # products = models.ManyToManyField(Product)
    total = models.DecimalField(decimal_places=2,max_digits=100,default = 0.00)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Cart id: {self.id}"
