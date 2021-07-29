from django.contrib import admin
from .models import Payment

# register Payment model for admin dashboard
admin.site.register(Payment)