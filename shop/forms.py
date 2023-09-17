from django.forms import ModelChoiceField, ModelForm, Select

from shop.models import Shop, Employee

class ShopForm(ModelForm):
    class Meta:
        model = Shop
        fields = ('address', 'number',)

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'position', 'shop']
    shop = ModelChoiceField(queryset=Shop.objects.all(), widget=Select(attrs={'class': 'form-control'}))
        