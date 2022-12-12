from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User


class APITest(TestCase):
    def test_user_auth(self):
        self.user = User.objects.create_user(username='admin', password='12345')

        resp = self.client.post('http://127.0.0.1:8000/api/v1/token/', data={'username': 'admin', 'password': '12345'})
        self.assertEqual(resp.status_code, 200)

        token =str('JWT' + resp.data['access'])

        client = APIClient()
        client.force_authenticate(user=self.user)

        response = client.get('http://127.0.0.1:8000/api/v1/menu/?day=monday', format='json', headers={'Authorization': token} )
        self.assertEqual(response.status_code, 200)