from django.contrib import admin
from .models import Product, Type, Cart, Order

class TypeAdmin(admin.ModelAdmin):
	list_display = ['name','price','product_code']
	class Meta:
		model = Type

class OrderAdmin(admin.ModelAdmin):
	list_display = ['id','total','date_added','date_updated','address']
	class Meta:
		model = Order	

class CartAdmin(admin.ModelAdmin):
	list_display = ['id','order','name','product_code','small_size','medium_size','large_size','no_size','date_added']
	class Meta:
		model = Cart

admin.site.register(Product)
admin.site.register(Type, TypeAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)