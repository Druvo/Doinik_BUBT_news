from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from Core.models import User


class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, null=True)
    organization = models.CharField(
        max_length=255, null=True, help_text='ex: Tiger Park Limited'
    )
    designation = models.CharField(
        max_length=120, null=True, help_text='ex: Software Engineer'
    )
    phone_no = models.CharField(max_length=11, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.email)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    phone_no = models.CharField(max_length=11, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.email)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Creates or updates profile, when User object changes"""
    if created and instance.user_type is 2:
        StaffProfile.objects.get_or_create(user=instance)

    if created and instance.user_type is 1:
        UserProfile.objects.get_or_create(user=instance)
