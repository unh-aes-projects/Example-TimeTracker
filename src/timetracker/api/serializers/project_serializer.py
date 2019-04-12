from rest_framework.serializers import ModelSerializer

from timetracker.models import Project


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'name',
            'description',
            'user')
