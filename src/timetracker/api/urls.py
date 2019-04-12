from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path(
        'project/<int:user>/',
        views.ProjectAPIView.as_view(),
        name='project'),
]
