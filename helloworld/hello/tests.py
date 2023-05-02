from django.test import TestCase

# Create your tests here.


class HelloWorldTestCase(TestCase):
    def test_hello_world_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, World!")
