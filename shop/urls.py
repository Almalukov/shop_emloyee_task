from django.urls import path

from shop.views import (EmployeeDeleteView, 
                        EmployeeListView, 
                        EmployeeUpdateView, 
                        ShopListView,
                        ShopCreateView,
                        ShopDeleteView,
                        EmployeeCreateView, ShopUpdateView,EmployeeShopListView)

urlpatterns = [
    path("", ShopListView.as_view(), name="shop-list"),
    path("create/", ShopCreateView.as_view(), name="shop-create"),
    path("delete/<int:pk>", ShopDeleteView.as_view(), name="shop-delete"),
    path('shops/<int:pk>/update/', ShopUpdateView.as_view(), name='shop-update'),
    path("create_employee/", EmployeeCreateView.as_view(), name="employee-create"),
    path("employees/", EmployeeListView.as_view(), name="employee-list"),
    path("shop/<int:shop_id>/employees/", EmployeeShopListView.as_view(), name="shop_employees"),
    path("delete_employee/<int:pk>", EmployeeDeleteView.as_view(), name="employee-delete"),
    path("employee/<int:pk>/update/", EmployeeUpdateView.as_view(), name="employee-update"),
]

