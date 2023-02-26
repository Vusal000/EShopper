from django.test import TestCase

from core.models import subscribe


class SubscribeModelTest(TestCase):

    def setUp(self):
        self.date1 = subscribe.objects.create(
            email = 'vusal@gmail.com',
        )

    def test_subscribe(self):
        self.assertEqual(self.date1.email,'vusalll@gmail.com')

    def tearDown(self):
        del self.date1


























