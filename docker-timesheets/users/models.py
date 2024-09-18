from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from log_config import logger


class CustomUser(AbstractUser):
    """
    This model extends Django's default AbstractUser model, allowing for custom user fields.
    """
    # custom email field to set it to unique and compulsory
    email = models.EmailField(unique=True, blank=False)
    # Custom field to track whether the user has been approved or not.
    is_approved = models.BooleanField(default=False)

    # String representation of the user, which will return the username when the object is printed or displayed.
    def __str__(self):
            return self.username
    
    # Method to assign the user to the 'TIMESHEETS LIMITED' group.
    # This will be called whenever the user is created or needs to be assigned to this group.
    def assign_initial_group(self):
        try:
            # Attempt to retrieve the group named 'REPORTER'.
            group = Group.objects.get(name='REPORTER')
            # Add the user to the retrieved group.
            self.groups.add(group)
            # Log a success message if the group assignment is successful.
            logger.debug(f"Assigned {self.username} to group 'REPORTER'.")
        except Group.DoesNotExist:
            # Log an error message if the group doesn't exist in the database.
            logger.error("Group 'REPORTER' does not exist.")

        
class UserProfile(models.Model):
    """
    The UserProfile model extends the user's data by adding extra fields like bio, resume, and avatar.
    Each CustomUser has one related UserProfile.
    """
    # Link the UserProfile to a CustomUser using a OneToOneField, meaning each user will have exactly one profile.
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='userprofile')
    
    # A field to store the user's biography. It's optional, so it can be left blank.
    bio = models.TextField(blank=True)
    
    # A field to upload the user's resume. The file will be uploaded to the 'cv/' directory.
    # This field is optional, allowing the user to skip uploading a resume.
    resume = models.FileField(upload_to='cv/', blank=True, null=True)
    
    # A field to upload the user's profile picture (avatar). The image will be uploaded to the 'avatars/' directory.
    # This field is also optional.
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    # String representation of the UserProfile, returning the username of the related user.
    def __str__(self):
        return self.user.username


