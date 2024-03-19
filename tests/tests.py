from django.test import TestCase


class URLTest(TestCase):

    def urltesting(self):
        response = self.client.get('/gfgfhgfhg/')
        self.assertEqual(response.status_code, 200)