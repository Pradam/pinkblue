from django.contrib import admin
from .models import (Vendor, Product,
	                 Batch, Inventory,
	                 InventoryModify)
# Register your models here.

admin.site.register((Vendor, Product,
	                 Batch, Inventory,
	                 InventoryModify))