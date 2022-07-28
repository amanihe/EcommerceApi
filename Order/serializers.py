from rest_framework import serializers
from Order.models import *


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = T_Order
        fields='__all__'


class SousOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=T_SousOrder
        fields='__all__'


class OrderLigneSerializer(serializers.ModelSerializer):
    class Meta:
        model = T_OrderLigne
        fields='__all__'

class FactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = T_Facture
        fields='__all__'
