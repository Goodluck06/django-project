from django.forms import ModelForm
from .models import Product, Orders, Expenses

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields =  '__all__'

class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields =  '__all__'

class MatumiziForm(ModelForm):
    class Meta:
        model = Expenses
        fields =  '__all__'
