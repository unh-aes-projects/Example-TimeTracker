from rest_framework.serializers import ModelSerializer

from timetracker.models import TimeEvent


class TimeEventSerializer(ModelSerializer):
    class Meta:
        model = TimeEvent
        fields = (
            'start_datetime',
            'end_datetime',
            'comments')
