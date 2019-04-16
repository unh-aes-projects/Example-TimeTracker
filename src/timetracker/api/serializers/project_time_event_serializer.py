from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)

from timetracker.models import Project
from .time_event_serializer import TimeEventSerializer


class ProjectTimeEventSerializer(ModelSerializer):

    time_events = SerializerMethodField()

    class Meta:
        model = Project
        fields = (
            'name',
            'description',
            'user',
            'time_events')

    def get_time_events(self, obj):
        """
        Returns the time_events related children
        queryset for the given project
        @param obj : Project object
        """
        time_event_qs = obj.timeevent_set.all()
        return TimeEventSerializer(time_event_qs, many=True).data
