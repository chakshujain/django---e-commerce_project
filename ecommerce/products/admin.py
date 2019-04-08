from django.contrib import admin
# Register your models here.
from products.models import Product,ProductImage,Variation

class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    search_fields = ['title','description']
    list_display = ['title','price','active','updated']
    list_editable = ['price','active']
    list_filter = ['price','active']
    readonly_fields = ['timestamp','updated']
    prepopulated_fields = {"slug":("title",)}
    class meta():
        model = Product
admin.site.register(ProductImage)
admin.site.register(Product,ProductAdmin)
admin.site.register(Variation)
