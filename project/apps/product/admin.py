from django.contrib import admin

from .models import (Product,
                     ProductComments,
                     ProductLikes
                     )


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(ProductLikes)
class AdminProduct(admin.ModelAdmin):
    list_display = ('product', 'user')


admin.site.register(ProductComments)
