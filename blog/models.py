from django.db import models
from django.utils import timezone


class Blog(models.Model):
    """ A blog post
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True,
                                          default=timezone.now)
    updated = models.DateTimeField(auto_now=True, blank=True)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='media/blogimage/',
                              blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Blog'
