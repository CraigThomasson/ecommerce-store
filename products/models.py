from django.db import models


class Category(models.Model):
    """
    baisc modle for product cetegories
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    baisc modle for products
    """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
    )
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    image = models.ImageField(null=True, blank=True, default='placeholder')
    colour = models.CharField(max_length=100, default='white')
    scent = models.CharField(max_length=100, default='unscented')

    def __str__(self):
        return self.name
