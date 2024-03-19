from django.test import TestCase

# Create your tests here.

class URLTest(TestCase):
    def urltesting(self):
        import pdb
        pdb.set_trace()
        response = self.client.get('/accohghgjhgjunt/')
        self.assertEqual(response.status_code, 200)
