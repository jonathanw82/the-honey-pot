from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class User_Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, null=False,
                                 blank=False)
    street_address1 = models.CharField(max_length=80, null=False,
                                       blank=False)
    street_address2 = models.CharField(max_length=80, null=False,
                                       blank=False)
    town_or_city = models.CharField(max_length=40, null=False,
                                    blank=False)
    county = models.CharField(max_length=80, null=False,
                              blank=False)
    postcode = models.CharField(max_length=20, null=False,
                                blank=False)
    phone_number = models.CharField(max_length=20, null=False,
                                    blank=False)
    dob = models.DateField(max_length=10, null=True, blank=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'User Profile'


@receiver(post_save, sender=User)
def create_or_update_User_Profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    # if created:
    User_Profile.objects.create(user=instance)
    # Existing users: just save the profile
    # instance.user_profile.save()
