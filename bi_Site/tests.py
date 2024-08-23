from django.test import TestCase

# Create your tests here.
from bi_Site.models import *
from django.contrib.auth.models import User

class Service(TestCase):
    def setup(self):
        self.service = Service.objects.create(
            title = 'Test Service',
            description = 'This is a test service',
            image = 'test_image.jpg'
        )
    
    def test_service_creation(self):
        self.assertEqual(self.service.title, 'Test Service')
        self.assertEqual(self.service.description, 'This is a test service')