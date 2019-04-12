from django.db import models


class TimeEvent(models.Model):
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    comments = models.CharField(max_length=255)
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        null=True)

    def __str__(self):
        return "{} ({}):({})".format(
            self.project,
            self.start_datetime,
            self.end_datetime
        )
