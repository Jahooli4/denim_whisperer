from django.contrib import admin
from .models import Product, Category


# class ProductGalleryInline(admin.TabularInline):
#     model = ProductGallery
#     extra = 5

#     def image_preview(self, obj):
#         if obj.image:
#             return format_html(
#                 '<img src="{}" width="50" height="50" />', obj.image.url)
#         return "No Image"

#     image_preview.allow_tags = True
#     image_preview.short_description = "Image Preview"


class ProductAdmin(admin.ModelAdmin):
    list_display = (

        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)

    # inlines = [ProductGalleryInline]

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(ProductGallery)
