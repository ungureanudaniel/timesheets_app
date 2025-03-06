from django.db import models
import datetime as dt

class ActivityProgram(models.Model):
    user = models.CharField(max_length=300)
    registration_nr = models.IntegerField()
    registration_date = models.DateField(default=dt.date.today())
    week = models.DateTimeField(default=dt.date.today().isocalendar()[1])
    activity_code = models.CharField(max_length=6)
    activity_title = models.CharField(max_length=300)

    def __str__(self):
        return "{} - {}".format(self.activity_code, self.activity_title)

