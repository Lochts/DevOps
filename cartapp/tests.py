from django.test import TestCase
from .views import re_email

class CartOrderTests(TestCase):

    def test_error_mail(self):
        customer = dict()
        customer['CustomerName'] = 'tester'
        customer['CustomerPhone'] = '0800000000'
        customer['CustomerAddress'] = '台中市西屯區文華路100號'
        customer['paytype'] = 'ATM 轉帳'

        customer['CustomerEmail'] = 'tester@mail.fcu.edu.tw'
        r = self.client.post('/cartok/', customer)
        self.assertEqual(r.status_code, 200)

        customer['CustomerEmail'] = 'tester#mail.fcu.edu.tw'
        r = self.client.post('/cartok/', customer)
        self.assertEqual(r.status_code, 302)
        self.assertEqual(r.url, '/cartorder/')
