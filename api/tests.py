from django.test import TestCase
from rest_framework.test import APIRequestFactory
from requests.auth import HTTPBasicAuth
from rest_framework.test import RequestsClient
from .models import *
# Create your tests here.
def setUp(self):
        # Create superuser
        self.user = User.objects.create_superuser(
        username='new_user', email='test@example.com', password='password',
        )
        # Set server client

def test_response():
    client = RequestsClient()
    url = 'https://peppertools.herokuapp.com'
    request = client.post(f'{url}/api/app/api/login', {"username":"lauro", "password": "mac_coder2002"})
    print(request)
    assert request.status_code == 200


    client.headers.update({'bearer': request.body.access})
