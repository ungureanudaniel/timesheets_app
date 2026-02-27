from django.contrib import admin
from .models import ActivityProgram

@admin.register(ActivityProgram)
class ActivityProgramAdmin(admin.ModelAdmin):
    list_display = ['activity_code', 'activity_title', 'registration_date', 'week', 'user']
    list_filter = ['registration_date', 'activity_code']
    search_fields = ['activity_code', 'activity_title', 'registration_nr']
    readonly_fields = ['week', 'year', 'created_at', 'updated_at']
    
    def week(self, obj):
        return obj.week
    week.short_description = 'Week'
    
    def year(self, obj):
        return obj.year
    year.short_description = 'Year'