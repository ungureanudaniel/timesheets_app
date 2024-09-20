from django.contrib.auth.models import AbstractUser, BaseUserManager, Group
from django.db import models
import logging

logger = logging.getLogger(__name__)


# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False)
    is_approved = models.BooleanField(default=False)
    is_person = models.BooleanField(default=True)
    bio = models.TextField(default="Write a short biography", blank=True)
    resume = models.FileField(upload_to='cv/', blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    # objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # or [] if you don't want to require username

    def __str__(self):
        return self.username

    def assign_initial_group(self):
        try:
            group = Group.objects.get(name='REPORTER')
            self.groups.add(group)
            logger.debug(f"Assigned {self.username} to group 'REPORTER'.")
        except Group.DoesNotExist:
            logger.error("Group 'REPORTER' does not exist.")
