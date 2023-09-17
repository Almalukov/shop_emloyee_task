from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from shop.models import Employee, Shop, ShopEmployee
from shop.forms import EmployeeForm, ShopForm


class ShopListView(ListView):
    model = Shop
    template_name = 'shop/shop_list.html'
    context_object_name = 'shops'

class ShopCreateView(CreateView):
    model = Shop
    form_class = ShopForm
    template_name = 'shop/shop_create.html'
    success_url = '/'

class ShopDeleteView(DeleteView):
    model = Shop
    success_url = reverse_lazy("shop-list")
    template_name = 'shop/shop_confirm_delete.html'

class ShopUpdateView(UpdateView):
    model = Shop
    form_class = ShopForm
    template_name = 'shop/shop_update.html'
    success_url = reverse_lazy("shop-list")
    
class EmployeeListView(ListView):
    model = Employee
    template_name = 'shop/employee_list.html'
    context_object_name = 'employees'

class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'shop/employee_create.html'
    success_url = reverse_lazy("employee-list")

    def form_valid(self, form):
        shop_id = int(form.data['shop'])
        self.object = form.save()
        ShopEmployee.objects.create(shop_id=shop_id, employee_id=self.object.id)
        return HttpResponseRedirect(self.get_success_url())

class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy("employee-list")
    template_name = 'shop/employee_confirm_delete.html'

class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'shop/employee_update.html' 
    success_url = reverse_lazy("employee-list")

class EmployeeShopListView(EmployeeListView):
    def get_queryset(self):
        return Employee.objects.filter(shop_employees__shop__id=self.kwargs['shop_id'])



