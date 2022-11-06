from django.db import models

# Create your models here.


class Products(models.Model):
    product_name = models.CharField(max_length=500)
    product_desc = models.TextField()
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    product_image = models.ImageField(upload_to='product-img/', null=True)
