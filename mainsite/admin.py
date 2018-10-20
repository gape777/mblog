from django.contrib import admin
from .models import Post, NewTable, Product

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'qty')


admin.site.register(Post, PostAdmin)
admin.site.register(NewTable)
admin.site.register(Product, ProductAdmin)
