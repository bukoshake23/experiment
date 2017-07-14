from django import forms


	
class TypeForm(forms.Form):
	small_size = forms.IntegerField(label='Small Size',required=False,min_value=1,widget=forms.NumberInput(attrs={'class':'form-control'}))
	medium_size = forms.IntegerField(label='Medium Size',required=False,min_value=1,widget=forms.NumberInput(attrs={'class':'form-control'}))
	large_size = forms.IntegerField(label='Large Size',required=False,min_value=1,widget=forms.NumberInput(attrs={'class':'form-control'}))
	no_size = forms.IntegerField(label='Quantity',required=False,min_value=1,widget=forms.NumberInput(attrs={'class':'form-control'}))
	name = forms.CharField(widget=forms.HiddenInput)	
	price = forms.FloatField(widget=forms.HiddenInput)
	product_code = forms.CharField(widget=forms.HiddenInput)

class CartForm(forms.Form):		
	address = forms.CharField(label='Address',max_length=200,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	total = forms.FloatField(widget=forms.HiddenInput)
	phone_number = forms.CharField(label='Phone Number',max_length=50,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))