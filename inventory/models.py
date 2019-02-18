from django.db import models

# Create your models here.

OPTIONAL = {'blank': True, 'null': True}

INVENTORY_CHOICE = ((0, 'Approved'),
                    (1, 'Pendind'))

INVENTORY_TYPE = ((0, 'Add'),
                  (1, 'Update'),
                  (2, 'Remove'))

class BaseContent(models.Model):
    ACTIVE_CHOICES = ((0, 'Inactive'), (2, 'Active'),)
    active = models.PositiveIntegerField(choices=ACTIVE_CHOICES,
                                         default=2)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def switch(self):
        self.active = {2: 0, 0: 2}[self.active]
        self.save()

    def __str_(self):
        return self.name


class Vendor(BaseContent):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.name)


class Product(BaseContent):
    name = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Batch(BaseContent):
    btchnum = models.PositiveIntegerField(default=0)
    btchdate = models.DateField()

    def __str__(self):
        return '%d' % (self.btchnum)


class Inventory(BaseContent):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    created_by = models.ForeignKey('auth.user', on_delete=models.CASCADE,
                                   **OPTIONAL)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE,)
    quantity = models.PositiveIntegerField(default=0)
    mrp = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.product.name


class InventoryModify(BaseContent):
    requested_by = models.ForeignKey('auth.user',
                                     on_delete=models.CASCADE,
                                     **OPTIONAL)
    stock_type = models.IntegerField(choices=INVENTORY_TYPE, default=0)
    inventory = models.ForeignKey(Inventory,
                                  on_delete=models.CASCADE,
                                  **OPTIONAL)
    status = models.IntegerField(choices=INVENTORY_CHOICE, default=1)

    def __str__(self):
        return '%s %s' % (self.get_stock_type_display(),
                          self.get_status_display())
