from django.test import TestCase
from rest_framework.test import APIClient

from .models import Item

class AddItemTestCase(TestCase):
    def setUp(self):
        self.factory = APIClient()

    def test_add_item(self):
        request_body = {
            'itemName': 'ITEM_NAME',
            'description': 'DESCRIPTION',
            'amount': 1
        }

        # Make API call for adding an item
        response = self.factory.post('/item/', request_body, format='json')
        
        # Check that response body was correct
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [request_body])

        # Check that an item was created
        items_count = Item.objects.all().count()
        self.assertEqual(items_count, 1)

        # Check contents of the first item
        new_item = Item.objects.first()
        self.assertEqual(new_item.item_name, request_body['itemName'])
        self.assertEqual(new_item.description, request_body['description'])
        self.assertEqual(new_item.amount, request_body['amount'])


class GetRemoveItemsTestCase(TestCase):
    def setUp(self):
        self.factory = APIClient()
        self.expected_response_body = []

        # Create expected response body with 3 items
        for i in range(3):
            item_index = str(i)
            self.expected_response_body.append({
                'itemName': 'ITEM_NAME_{}'.format(item_index),
                'description': 'DESCRIPTION_{}'.format(item_index),
                # 0 is not a valid amount
                'amount': i + 1,
            })

        # Use expected response body to create objects in database
        for item_dict in self.expected_response_body:
            Item.objects.create(
                item_name=item_dict['itemName'],
                description=item_dict['description'],
                amount=item_dict['amount']
            )

    def test_get_items(self):
        # Make API call for getting items
        actual_response_body = self.factory.get('/item/', format='json')

        # Check that response body was correct
        self.assertEqual(actual_response_body.status_code, 200)
        self.assertEqual(actual_response_body.data, self.expected_response_body)

    def test_delete_item(self):
        delete_id = Item.objects.all()[1].id

        # Make API call for removing items
        request_body = {'id': str(delete_id)}
        response = self.factory.post('/item/delete/', request_body, format='json')
        self.assertEqual(response.status_code, 200)

        # Verify that there is one less item in the database
        num_items = len(Item.objects.all())
        self.assertEqual(2, num_items)