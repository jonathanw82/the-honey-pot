from django.db import models
from django.contrib.auth.models import User


class Profiles(models.Model):



    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Profiles'