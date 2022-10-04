from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(CategoryModel)
admin.site.register(ImageProductModel)

class ImageItemLine(admin.TabularInline):
    model = ImageProductModel


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ImageItemLine,)



# class OrderItemsLine(admin.TabularInline):
#     model = OrderItemsModel

# @admin.register(OrderModel)
# class OrderAdmin(admin.ModelAdmin):
#     list_display=('user',)
#     inlines = (OrderItemsLine,)
admin.site.register(OrderItemsModel)
admin.site.register(OrderModel)

admin.site.register(BrandModel)
admin.site.register(ProductNotModels)
admin.site.register(TypeProductModel)
admin.site.register(ImagdeSlidModel)
