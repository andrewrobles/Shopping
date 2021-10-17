from django.test import TestCase
from rest_framework.test import APIClient

from .models import Item

class ShoppingTestCase(TestCase):
    def setUp(self):
        self.factory = APIClient()

    def test_hello_world(self):
        response_body = {
            'message': 'Hello, world!!'
        }

        response = self.factory.get('/hello-world/', format='json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, response_body)

    def test_add_item(self):
        request_body = {
            'itemName': 'ITEM_NAME',
            'description': 'DESCRIPTION',
            'amount': 1
        }

        # Make API call for adding an item
        response = self.factory.post('/add-item/', request_body, format='json')
        
        # Check that response body was correct
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, request_body)

        # Check that an item was created
        items_count = Item.objects.all().count()
        self.assertEqual(items_count, 1)

        # Check contents of the first item
        new_item = Item.objects.first()
        self.assertEqual(new_item.item_name, request_body['itemName'])
        self.assertEqual(new_item.description, request_body['description'])
        self.assertEqual(new_item.amount, request_body['amount'])

        



        
