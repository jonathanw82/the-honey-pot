from django.db import models
# from datetime import datetime, date


class Products(models.Model):

    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=1)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    image = models.ImageField(upload_to='media/images/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products'
