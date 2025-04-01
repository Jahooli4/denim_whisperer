from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Subcategory(models.Model):

    class Meta:
        verbose_name_plural = 'Subcategories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    subcategory = models.CharField(max_length=254, null=True, blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, blank=True)
    image = CloudinaryField('image', blank=True)

    def __str__(self):
        return self.name

class ProductGallery(models.Model):

    class Meta:
        verbose_name_plural = 'Product Galleries'
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="gallery")
    image = CloudinaryField('image', null=True, blank=True)

    def __str__(self):
        return f"Image for {self.product.name}"