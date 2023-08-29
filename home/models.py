from django.db import models
from datetime import date

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    unit = models.CharField(max_length=50)
    buying_price = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    in_out = models.CharField(max_length=4, default='out')
    date_added = models.DateTimeField(auto_now=True)

    def day_added(self):
        # today = date.today().strftime('%A')
        # added_day = self.date_added.strftime('%A')
        # if today == added_day:
        #     return True
        # else:
        return self.date_added.strftime('%A')

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)

class Expenses(models.Model):
    matumizi_id = models.AutoField(primary_key=True)
    details = models.CharField(max_length=200)
    amount = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now=True)

    def day_added(self):
        return self.date_added.strftime('%A')

    def __str__(self):
        return self.details
