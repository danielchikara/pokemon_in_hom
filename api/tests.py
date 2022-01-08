from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from api.models import *
import json

# Create your tests here.


class UserTestCase(TestCase):
    def setUp(self):
        user = User(
            email='chikara@test.com',
            first_name='Testing',
            last_name='Testing',
        )
        user.set_password('rc{4@qHjR>!b`yAV')
        user.save()
        self.client = APIClient()

    def test_register_user(self):
        response = self.client.post(
            '/api/register/client/', {
                'email': 'testing@chikara.com',
                'password': 'rc{4@qHjR>!b`yAV',
                'password_confirmation': 'rc{4@qHjR>!b`yAV',
            },
            format='multipart'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content), {'success': True})