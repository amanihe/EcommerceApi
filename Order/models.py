from datetime import datetime
from itertools import product
from django.db import models

from Accounts.models import *


from Products.models import *
ORDER_STATUS_CHOICES = (
    ('créée', 'Créée'),
    ('envoyée', 'Envoyée'), #just for supplier
    ('payée', 'Payée'),
    ('en livraison', 'En livraison'),
    ('livrée', 'Livrée')
)
ORDERLIGN_STATUS_CHOICES = (
  ('créée', 'Créée'),
  ('envoyée', 'Envoyée'),
    ('en livraison', 'En livraison'),
    ('livrée', 'Livrée'),
    ('payée', 'Payée')
)
ORDER_TYPE_CHOICES = (
    ('customer', 'Customer'),
    ('admin', 'Admin')
)


class T_Order(models.Model):
    Ord_Id = models.AutoField(primary_key=True)
    User = models.ForeignKey(
        T_User, on_delete=models.CASCADE, related_name='User_Order')
    Ord_Type = models.CharField(max_length=120, choices=ORDER_TYPE_CHOICES)
    Ord_Status = models.CharField(
        max_length=120, default='créée', choices=ORDER_STATUS_CHOICES)
    Ord_Date = models.DateTimeField(auto_now_add=True)


class T_OrderLigne(models.Model):
    OrdLign_Id = models.AutoField(primary_key=True)
    Order = models.ForeignKey(T_Order, null=True,
                              on_delete=models.CASCADE)
    Product = models.ForeignKey(T_Product,
                                on_delete=models.CASCADE)
   
    Ord_Qte = models.IntegerField()
    Supplier = models.ForeignKey(
        T_User, on_delete=models.CASCADE,null=True, related_name='Supplier_Order')
    OrdLign_Status = models.CharField(
        max_length=120, default='créée',null=True, choices=ORDERLIGN_STATUS_CHOICES )
    Create_at = models.DateTimeField(auto_now_add=True)



class T_Facture(models.Model):
    Fact_Id = models.AutoField(primary_key=True)
    Fact_Num = models.CharField(max_length=150)

    Fact_OrderCost = models.DecimalField(
        decimal_places=2, max_digits=20, default=0)
    Fact_Discount = models.IntegerField()
    Fact_CostFinal = models.DecimalField(
        decimal_places=2, max_digits=20, default=0)
    Fact_Type = models.CharField(max_length=150)
    Create_at = models.DateTimeField(auto_now_add=True)
