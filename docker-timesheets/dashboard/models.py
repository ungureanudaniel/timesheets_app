from django.db import models
import datetime as dt
from django.utils import timezone
from django.conf import settings

class ActivityProgram(models.Model):
    """Model for tracking activity programs"""
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='activity_programs',
        null=True,  # Allow null for now
        blank=True
    )
    registration_nr = models.CharField(
        max_length=50, 
        unique=True,
        help_text="Unique registration number"
    )
    registration_date = models.DateField(default=timezone.now)
    activity_code = models.CharField(max_length=6, db_index=True)
    activity_title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def week(self):
        """Get ISO week number from registration date"""
        if self.registration_date:
            _, week_num, _ = self.registration_date.isocalendar()
            return week_num
        return 0
    
    @property
    def year(self):
        """Get year from registration date"""
        if self.registration_date:
            return self.registration_date.year
        return 0
    
    def __str__(self):
        return f"{self.activity_code} - {self.activity_title}"
    
    class Meta:
        verbose_name = "Activity Program"
        verbose_name_plural = "Activity Programs"
        ordering = ['-registration_date', 'activity_code']
        indexes = [
            models.Index(fields=['activity_code']),
            models.Index(fields=['registration_date']),
        ]
