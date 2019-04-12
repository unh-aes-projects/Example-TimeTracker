from django.contrib.auth.models import User
from django.db import models


class TimeEvent(models.Model):
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_id = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        null=True)
