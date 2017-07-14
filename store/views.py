from django.views import generic
from django.shortcuts import render
from .models import Product, Type, Order, Cart
from .forms import CartForm, TypeForm



class IndexView(generic.ListView):
	template_name = 'store/index.html'
	context_object_name = 'products'

	def get_queryset(self):
		return Product.objects.all()


def TypesView(request,product_id):
	p = Product.objects.get(pk=product_id)
	types = p.type_set.all()
	products = Product.objects.all()
	error_message = []	
	cart = False

	if request.method == 'POST':
		form = TypeForm(request.POST)		
		if form.is_valid():			

			# ------------ validations ---------------

			quantity_fields = ['small_size','medium_size','large_size','no_size']

			error_message.append("Please enter quantity then click Add to Cart.")									
			for field in quantity_fields:								
				if form.cleaned_data[field]:
					error_message = []
					break

			# ------------ caching orders -------------
					
			if not error_message:
				item_data = {}
				for key,value in form.cleaned_data.items():			
					if form.cleaned_data[key]:
						item_data[key] = value								
				ctr = 1	
				item_num = ''
				while(1):
					item_num = 'item'+str(ctr)
					if not item_num in request.session.keys():
						break
					ctr+=1		
				request.session[item_num] = item_data			
				request.session.set_expiry(300)
				request.session.clear_expired()				
			
			
	
	form = TypeForm()
	
	for key, value in request.session.items():
		if key.startswith('item'):
			cart = True

	context = {	
		'types':types,
		'products':products,
		'product_id':product_id,		
		'form': form,
		'error_message': error_message,
		'cart':cart
	}
	

	return render(request, 'store/types.html', context)


def CartView(request):	
	products = Product.objects.all()

	# ------------ delete order ------------

	if request.method == 'POST':
		if request.POST['item_delete'] in request.session.keys():
			del request.session[request.POST['item_delete']]

	# ------------ getting total amount ------------

	total = 0	
	for item, data in request.session.items():
		if item.startswith('item'):			
			quantity = 0
			quantity_fields = ['small_size','medium_size','large_size','no_size']			
			for key, value in data.items():				
				if key in quantity_fields:
					quantity += value					
			total = round(total + (data['price'] * quantity),2)


	form = CartForm()
	
	context = {			
		'products':products,
		'total':total,	
		'form':form,		
	}


	
	return render(request, 'store/cart.html',context)

	


def CheckOutView(request):
	products = Product.objects.all()	
	template_name = 'store/index.html'
	out_stock = False
	supply_quantity_display = {}
	if request.method == 'POST':
		form = CartForm(request.POST)	
		if form.is_valid():

			# ------------ summarizing total quantities ------------

			cart_summary = {}
			for item, data in request.session.items():
				if item.startswith('item'):
					if not data['product_code'] in cart_summary.keys():
						cart_summary[data['product_code']] = {}
					for data_key in data.keys():
						if data_key.endswith('_size'):
							size = data_key
							if not data_key in cart_summary[data['product_code']].keys():
								cart_summary[data['product_code']][size] = 0
							cart_summary[data['product_code']][size] += data[size]


			# ------------ checking order quantity vs supply quantity ------------


			for product_code, data in cart_summary.items():
				type_obj = Type.objects.get(product_code=product_code)
				supply_quantity = {'small_size':type_obj.small_size,'medium_size':type_obj.medium_size,'large_size':type_obj.large_size,'no_size':type_obj.no_size}								
				for size, order_quantity in data.items():
					if not order_quantity <= supply_quantity[size]:					
						if size == 'no_size':
							supply_quantity_display[type_obj.name] = {'No Size':supply_quantity[size]}
						else:
							supply_quantity_display[type_obj.name] = {'Small Size':supply_quantity['small_size'],'Medium Size':supply_quantity['medium_size'],'Large Size':supply_quantity['large_size']}
						out_stock = True
			


			# ------------ recording order details ------------
							
								
			if not out_stock:
				delete_items = []
				order_obj = Order()
				order_obj.total = form.cleaned_data['total']
				order_obj.address = form.cleaned_data['address']
				order_obj.phone_number = form.cleaned_data['phone_number']
				order_obj.save()	
				for item, data in request.session.items():
					if item.startswith('item'):

						cart_obj = Cart()
						cart_obj.order = order_obj
						cart_obj.name = data['name']
						cart_obj.product_code = data['product_code']
						type_obj = Type.objects.get(product_code=data['product_code'])								

						if 'small_size' in data.keys():
							cart_obj.small_size = data['small_size']
							type_obj.small_size -= data['small_size']
						if 'medium_size' in data.keys():
							cart_obj.medium_size = data['medium_size']
							type_obj.medium_size -= data['medium_size']
						if 'large_size' in data.keys():
							cart_obj.large_size = data['large_size']
							type_obj.large_size -= data['large_size']
						if 'no_size' in data.keys():
							cart_obj.no_size = data['no_size']
							type_obj.no_size -= data['no_size']

						cart_obj.save()
						type_obj.save()

						delete_items.append(item)

				for item in delete_items:
					del request.session[item]
		

			template_name = 'store/checkout.html'	
		
	context = {
		'products':products,
		'out_stock':out_stock,
		'supply_quantity_display':supply_quantity_display,
	}


	return render(request,'store/checkout.html',context)
		

	





