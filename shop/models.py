from django.db import models

class Shop(models.Model):
    address = models.CharField(
        max_length=200
    )
    number = models.IntegerField()

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return self.address
        
class Employee(models.Model):
    name = models.CharField(
        max_length=200,
    )
    position = models.CharField(
        max_length=200
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        
class ShopEmployee(models.Model):
    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
        related_name='shop_employees'
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='shop_employees'
    )

    class Meta:
        verbose_name = 'Магазин-Сотрудник'
        verbose_name_plural = 'Магазины-Сотрудники'
