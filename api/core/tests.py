from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status

CREATE_OUTLIER_URL = reverse('create_outliers')
class TestOutlier(TestCase):
    '''Create a new Outlier'''

    def setUp(self):
        self.client = APIClient()

    def test_create_outlier_success(self):
        '''Test creating a new Outlier'''

        payload = {
            'project_name': 'RaizenOutlier',
            'table_name': 'Values',
            'outlier': '1 0.6'
        }

        res = self.client.post(CREATE_OUTLIER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    
    
class ListOutlier(TestCase):
    '''List Outliers registered'''

    def setUp(self):
        self.client = APIClient()
        payload = {
            'project_name': 'RaizenOutlier',
            'table_name': 'Values',
            'outlier': '1 0.6'
        }

        self.client.post(CREATE_OUTLIER_URL, payload)

    def test_create_outlier_success(self):
        '''Test Listining Outliers'''

        res = self.client.get('/api/list_outliers/RaizenOutlier/Values/')

        self.assertEqual(res.status_code, status.HTTP_200_OK)