from django.contrib import admin

from shop.models import Shop, Employee, ShopEmployee

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'address')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
admin.site.register(ShopEmployee)
