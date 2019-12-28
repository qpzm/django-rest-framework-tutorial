from django.test import TestCase
from ..models import Snippet


class ModelTestCase(TestCase):
    """This class defines the test suite for the bucketlist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.snippet = Snippet(code="print(123)")

    def test_model_can_create_a_bucketlist(self):
        """Test the snippet model can create a snippet."""
        old_count = Snippet.objects.count()
        self.snippet.save()
        new_count = Snippet.objects.count()
        self.assertNotEqual(old_count, new_count)
