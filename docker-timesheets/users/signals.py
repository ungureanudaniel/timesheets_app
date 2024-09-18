from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile, CustomUser
from django.contrib.auth import get_user_model
from log_config import logger

# # Signal to automatically create a UserProfile when a CustomUser is created
# @receiver(post_save, sender=CustomUser)
# def create_user_profile(sender, instance, created, **kwargs):
#     logger.info(f"New user account created for {instance.username}.")
#     if created:
#         UserProfile.objects.create(user=instance)

# # Signal to save the UserProfile when the CustomUser is saved
# @receiver(post_save, sender=CustomUser)
# def save_user_profile(sender, instance, **kwargs):
#     logger.info(f"New user account saved for {instance.username}.")
#     instance.userprofile.save()