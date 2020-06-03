from django.contrib import admin
from mptt.admin import MPTTModelAdmin
# Register your models here.
from .models import Product, Manufacturer, Category


admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Manufacturer)
admin.site.register(Product)



