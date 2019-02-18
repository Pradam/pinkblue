from rest_framework import serializers
from .models import Inventory

class InventorySerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')
    vendor_name = serializers.CharField(source='vendor.name')
    batch_number = serializers.CharField(source='batch.btchnum')
    batch_date = serializers.CharField(source='batch.btchdate')

    class Meta:
        model = Inventory
        fields = ('product_name', 'mrp',
                  'batch_number', 'batch_date',
                  'vendor_name', 'quantity',
                  'id')