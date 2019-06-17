from django.db import models
from login.models import UserProfile


class category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class product(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity_per_piece = models.CharField(max_length=100)
    quantity_in_stock = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="products", default="products/default")

    def __str__(self):
        return self.name


class order(models.Model):
    name = models.CharField(max_length=100)
    mobile_phone = models.CharField(max_length=100)
    Town = models.CharField(max_length=100)
    Address = models.CharField(max_length=1000)
    amount = models.IntegerField()

    def __str__(self):
        return self.name


class cart(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    order = models.ForeignKey(order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    checkout = models.BooleanField(default=False)


