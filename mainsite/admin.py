from django.contrib import admin
from .models import Post, NewTable, Product, PModel, Maker

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')


class MakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')


class PModelAdmin(admin.ModelAdmin):
    list_display = ('maker', 'name', 'url')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'price', 'description')


admin.site.register(Post, PostAdmin)
admin.site.register(NewTable)
admin.site.register(Maker, MakerAdmin)
admin.site.register(PModel, PModelAdmin)
admin.site.register(Product, ProductAdmin)
