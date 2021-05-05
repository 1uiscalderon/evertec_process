from django.test import TestCase
from app_v1.models import Order


class BasicTest(TestCase):
    def test_fields(self):
        order = Order()
        order.customer_name = "This is a test"
        order.customer_email = "test@gmail.com"
        order.customer_mobile = 12345123

        order.save()

        record = Order.objects.get(pk=1)
        self.assertEqual(record, order)
