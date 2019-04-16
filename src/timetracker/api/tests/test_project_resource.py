from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APIClient, APITestCase

from timetracker.api.serializers import (
    ProjectSerializer,
    ProjectTimeEventSerializer
)
from timetracker.models import Project


class ProjectResourceAPITests(APITestCase):
    """
    Tests all endpoints associated with a Project Resource
    """

    client = APIClient

    def setUp(self):
        # create a user
        user1 = User.objects.create_user(
            'user1',
            'user1@example.com',
            'user1password'
        )
        # create a project tied to user
        project1 = Project(
            name="project1_name",
            description="project1_description",
            user=user1)
        project1.save()

    def test_get_project(self):
        """
        No projects currently exist, should return empty json
        """
        user1 = User.objects.get(username='user1')
        # hit the endpoint
        response = self.client.get(
            reverse("timetracker:api:project", kwargs={"user": user1.id})
        )
        # check for 200 status code
        self.assertEqual(response.status_code, 200)

        # check that API response is same as user1.project_set.all()
        expected = user1.project_set.all()
        serialized = ProjectSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)

    def test_get_project_time_events_for_response_ok(self):
        """
        Tests the project_time_events endpoint using a get request
        for:
            200 Response Code
        """
        user1 = User.objects.get(username='user1')
        project1 = Project.objects.get(name='project1_name')
        # hit the endpoint
        response = self.client.get(
            reverse(
                "timetracker:api:project_time_events",
                kwargs={"project_id": project1.id})
        )
        # check for 200 status code
        self.assertEqual(response.status_code, 200)

    def test_get_project_time_events_response_for_keys(self):
        """
        Tests the project_time_events endpoint using a get request
        for the following keys in response:
            'name'
            'description'
            'user'
            'time_events'
        """
        user1 = User.objects.get(username='user1')
        project1 = Project.objects.get(name='project1_name')
        # hit the endpoint
        response = self.client.get(
            reverse(
                "timetracker:api:project_time_events",
                kwargs={"project_id": project1.id})
        )
        # The JSON response have 4 keys: name, description, user, time_events
        self.assertTrue('name' in response.data)
        self.assertTrue('description' in response.data)
        self.assertTrue('user' in response.data)
        self.assertTrue('time_events' in response.data)

    def test_get_project_time_events_response_for_keys(self):
        """
        Tests the project_time_events endpoint using a get request
        to check the 'time_events' key = the projects
        time events
        """
        user1 = User.objects.get(username='user1')
        project1 = Project.objects.get(name='project1_name')
        # hit the endpoint
        response = self.client.get(
            reverse(
                "timetracker:api:project_time_events",
                kwargs={"project_id": project1.id})
        )
        # check that API response is same as user1.project_set.all()
        expected = project1.timeevent_set.all()
        serialized = ProjectTimeEventSerializer(expected, many=True)
        # The JSON response have 4 keys: name, description, user, time_events
        # the time_events keys should be the list of all time events for that
        # project. check if response.data['time_events'] = expected
        self.assertQuerysetEqual(response.data['time_events'], expected)
