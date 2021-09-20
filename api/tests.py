from django.test import TestCase
from rest_framework.test import APIRequestFactory
from requests.auth import HTTPBasicAuth
from rest_framework.test import RequestsClient

# Create your tests here.

client = RequestsClient()
url = 'https://peppertools.herokuapp.com'
request = client.post(f'{url}/api/app/api/login', {"username":"lauro", "password": "mac_coder2002"})
print(request)
assert request.status_code == 200


client.headers.update({'bearer': request.body.access})
