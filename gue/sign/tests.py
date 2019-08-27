from django.test import TestCase
from .models import Event, Guest

# Create your tests here.

class ModelTest(TestCase):
    def setUp(self):
        Event.objects.create(id=6, name='one_plu3', status=True, limit=20,
                             address='shen_zhen', start_time='2019-08-01 02:18:11')
        Guest.objects.create(id=6, event_id=6, realname='alen',
                             phone='19000000004', email='alen@lifesense.com', sign=False)

    def test_event_models(self):
        result = Event.objects.get(name='one_plus3')
        self.assertEqual(result.address, 'shen_zhen')
        self.assertTrue(result.status)

    def test_guest_models(self):
        result = Guest.objects.get(phone='19000000004')
        self.assertEqual(result.realname, 'alen')
        self.assertFalse(result.sign)