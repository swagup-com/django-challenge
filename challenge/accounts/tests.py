from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Account
from django.contrib.auth.models import User
import base64
from rest_framework.test import RequestsClient
from requests.auth import HTTPBasicAuth
from django.urls import reverse
# Create your tests here.
class AccountTest(APITestCase):
    def setUp(self):
        # Create a Test User.
        self.test_user = User.objects.create_user('testuser', 'test@example.com','testpassword')
        # Set Up a Test Application
        # Create Entries in our model to fetch the list of.
        self.account = Account(
        name = 'aaa',
        phone = 'bbb',
        billing_address1 = 'cc',
        billing_address2 = 'dd',
        billing_city = 'ee',
        billing_state = 'ff',
        billing_zip = 'gg',
        billing_country = 'US',
        shipping_address1 = 'hh',
        shipping_address2 = 'ii',
        shipping_city = 'jj',
        shipping_state = 'kk',
        shipping_zip = 'll',
        shipping_country = 'ES'
        )

        self.account.save()

    def test_put_account(self):


        client = RequestsClient()
        r = client.get('http://localhost:8000/api/v1/accounts/', auth=HTTPBasicAuth('testuser', 'testpassword'))

        assert r.status_code == 200

        r = client.get('http://localhost:8000/api/v1/accounts/1', auth=HTTPBasicAuth('testuser', 'testpassword'))

        assert r.status_code == 200

        data = r.json()

        assert data['billing_city'] == 'ee'

        r = client.put('http://localhost:8000/api/v1/accounts/1/', auth=HTTPBasicAuth('testuser', 'testpassword'), json={'billing_city':'eeeee'})

        assert r.status_code == 200

        data = r.json()

        assert data['billing_city'] == 'eeeee'


    def test_fail_not_logged(self):

        client = RequestsClient()

        r = client.get('http://localhost:8000/api/v1/accounts/', auth=HTTPBasicAuth('testuser', 'sss'))

        assert r.status_code != 200