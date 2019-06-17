from django.contrib import admin
from .models import category, product, order, cart


admin.site.register(category)
admin.site.register(product)
admin.site.register(order)
admin.site.register(cart)

