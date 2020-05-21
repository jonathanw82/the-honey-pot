from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Review(models.Model):
    """ A review post
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.CharField(max_length=254)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=254)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True,
                                          default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Review'
