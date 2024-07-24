from django.contrib import admin
from myapp.models import Person, Customer, Product

# Register your models here.

class CurstomerAdmin(admin.ModelAdmin):
    list_display = ["document_number", "first_name", "last_name"]

class PersonAdmin(admin.ModelAdmin):
    list_display = ["id","document_number", "first_name", "last_name"]
    search_fields = [ "document_number","first_name", "last_name"]

class ProductAdmin(admin.ModelAdmin):
    list_display = ["id","product_code", "product_name", "brand", "model", "stock"]
    search_fields = ["product_code", "product_name", "brand", "model"]
    list_filter = ["brand"]

admin.site.register(Person, PersonAdmin)
admin.site.register(Customer, CurstomerAdmin)
admin.site.register(Product, ProductAdmin)
