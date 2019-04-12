from rest_framework.generics import ListCreateAPIView

from timetracker.api.serializers import ProjectSerializer
from timetracker.models import Project


class ProjectAPIView(ListCreateAPIView):
    lookup_url_kwarg = 'user'
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
