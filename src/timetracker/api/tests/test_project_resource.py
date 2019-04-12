from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APIClient, APITestCase

from timetracker.api.serializers import ProjectSerializer
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
