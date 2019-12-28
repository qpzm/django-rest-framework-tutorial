from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


class ViewTestCase(TestCase):
    pass
    """Test suite for the api views."""
    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.snippet_data = {'code': 'print(123)'}
        self.response = self.client.post(
            #reverse('snippet_list'),
            '/snippets/',
            self.snippet_data,
            format="json")

    def test_api_can_create_a_snippet(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
