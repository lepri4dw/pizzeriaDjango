from django.contrib import admin

from .models import DishListModel, Orders, Slider

admin.site.register(DishListModel)
admin.site.register(Orders)
admin.site.register(Slider)
