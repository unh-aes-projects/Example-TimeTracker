from rest_framework.generics import RetrieveAPIView

from timetracker.api.serializers import ProjectTimeEventSerializer
from timetracker.models import Project


class ProjectTimeEventsAPIView(RetrieveAPIView):
    lookup_url_kwarg = 'project_id'
    queryset = Project.objects.all()
    serializer_class = ProjectTimeEventSerializer
