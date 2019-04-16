from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path(
        'project/<int:user>/',
        views.ProjectAPIView.as_view(),
        name='project'),
    path(
        # TODO: add user kwarg to url to check object level permissions
        'project/events/<int:project_id>/',
        views.ProjectTimeEventsAPIView.as_view(),
        name='project_time_events'
    )
]
