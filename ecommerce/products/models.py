from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(max_length = 2000,blank=True)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    slug = models.SlugField(max_length=50,unique = True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        unique_together = ('title','slug')
    def get_absolute_url(self):
        return reverse("single_product",kwargs={"slug":self.slug})
    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images')
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title


class VariationManager(models.Manager):
    def all(self):
        return super(VariationManager,self).filter(active = True)
    def sizes(self):
        return self.all().filter(category = 'size')
    def colors(self):
        return self.all().filter(category = 'color')



VAR_CATEGORIES = (
('size','size'),
('color','color'),
('package','package'),
)

class Variation(models.Model):
    title = models.CharField(max_length = 100)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    category = models.CharField(max_length = 120,choices = VAR_CATEGORIES,default = 'size')
    image = models.ForeignKey(ProductImage,on_delete = models.CASCADE,null = True,blank = True)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    objects = VariationManager()

    def __str__(self):
        return self.title
