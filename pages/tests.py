from django.test import SimpleTestCase


class SimpleTestCases(SimpleTestCase):
    def test_home_page_response_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_response_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
