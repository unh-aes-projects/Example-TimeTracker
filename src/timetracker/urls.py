from django.urls import path, include

app_name = 'timetracker'
urlpatterns = [
    path('api/', include('timetracker.api.urls', namespace='api'))
]
