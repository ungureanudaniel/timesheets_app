from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from reports.models import MonthlyReport

class MonthlyReportAPITests(APITestCase):
    def setUp(self):
        # i create the test user here
        self.new_user = User.objects.create_user(username='test_user1', password='testpassword123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
    
        # create sample data
        self.report = MonthlyReport.objects.create(
            user=self.user,
            activity="1.2.3",
            description ="This is a test activity",

        )
