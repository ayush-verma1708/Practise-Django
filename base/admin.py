from django.contrib import admin
from .models import restaurant , items , restaurant_menu

# Register your models here.
admin.site.register(restaurant)
admin.site.register(items)
admin.site.register(restaurant_menu)