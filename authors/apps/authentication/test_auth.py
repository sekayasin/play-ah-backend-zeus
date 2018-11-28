from django.test import TestCase
from rest_framework import serializers, status
from rest_framework.test import APIClient


class AuthTestCase(TestCase):
    """
    Class with tests to do with registration views
    """

    def setUp(self):
        """Test registration and login api views"""
        self.client = APIClient()

        self.user = {"user": {"username": "eric",
                                   "email": "eric@gmail.com",
                                   "password": "incorrect"}}

        self.reg_token = {"user": 
                            {"username": "ekumamait",
                                "email": "ekumamait@gmail.com",
                                "password": "EkUmAmAiT"}}

        self.login_token = {"user": 
                                {"email": "eric@gmail.com", 
                                    "password": "incorrect"}}
        self.response = self.client.post(
            '/api/users/', self.user, format="json")

    def test_token_received_after_successfull_registration(self):
        """
        Test that a user will receive 
        a token after successfull registration
        """
        response = self.client.post(
            '/api/users/', self.reg_token, format="json")
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        assert "token" in response.data

    def test_token_received_after_successfull_login(self):
        """
        Test that a user will receive 
        a token after successfull login
        """
        response = self.client.post(
            '/api/users/login/', self.login_token, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert "token" in response.data
