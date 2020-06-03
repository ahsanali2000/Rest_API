from django.test import TestCase

from django.contrib.auth import get_user_model

User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        user=User.objects.create(username='ahsan',email='ahsan@gmail.com')
        user.set_password('ahsan')
        user.save()

    def test_created_user(self):
        qs=User.objects.filter(username='ahsan')
        self.assertEqual(qs.count(),1)