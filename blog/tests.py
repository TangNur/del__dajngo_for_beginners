from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from blog.models import PostTab


class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.post = PostTab.objects.create(
            title='ASDGFseAGdsgvx dsgfs',
            body='AFaeSfdsa asfas edfasd asfds as',
            author=self.user
        )

    def test_string_representation(self):
        post = PostTab(title='sadfsaf Wda sd as daw')
        self.assertEqual(str(post), post.title)
