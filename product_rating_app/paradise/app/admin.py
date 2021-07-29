from django.contrib import admin
from .models import Product, Review


""" Registering our models in admin panel"""

admin.site.register(Product)
admin.site.register(Review)
