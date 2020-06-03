from django.test import TestCase

from django.contrib.auth import get_user_model

from .models import Status
User = get_user_model()

class StatusTestCase(TestCase):
    def setUp(self):
        user=User.objects.create(username='ahsan',email='ahsan@gmail.com')
        user.set_password('ahsan')
        user.save()

    def test_created_status(self):
        user=User.objects.get(username='ahsan')
        obj=Status.objects.create(user=user, content='Some new content using test')
        self.assertEqual(obj.id,1)
        qs=Status.objects.all()
        self.assertEqual(qs.count(),1)