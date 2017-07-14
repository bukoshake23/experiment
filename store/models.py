from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=25)
	logo = models.FileField()

	def __str__(self):
		return self.name

class Type(models.Model):
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	name = models.CharField(max_length=25)
	description = models.CharField(max_length=500)
	price = models.DecimalField(decimal_places=2,max_digits=8)
	picture = models.FileField()	
	small_size = models.PositiveIntegerField(null=True, blank=True)
	medium_size = models.PositiveIntegerField(null=True, blank=True)
	large_size = models.PositiveIntegerField(null=True, blank=True)
	no_size = models.PositiveIntegerField(null=True, blank=True)
	product_code = models.CharField(max_length=25)

	
	def __str__(self):
		return self.name + ' - ' + str(self.price)

class Order(models.Model):
	total = models.DecimalField(decimal_places=2,max_digits=8, default=0)
	address = models.CharField(max_length=200)
	phone_number = models.CharField(max_length=50)
	date_added = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.pk)

class Cart(models.Model):
	order = models.ForeignKey(Order,on_delete=models.CASCADE)
	name = models.CharField(max_length=25)
	product_code = models.CharField(max_length=25)
	date_added = models.DateTimeField(auto_now_add=True)	
	small_size = models.PositiveIntegerField(null=True, blank=True)
	medium_size = models.PositiveIntegerField(null=True, blank=True)
	large_size = models.PositiveIntegerField(null=True, blank=True)
	no_size = models.IntegerField(null=True, blank=True)
	
	
	def __str__(self):
		return str(self.order) + ' - ' + self.product_code + ' - ' + str(self.date_added)


