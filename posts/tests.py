from django.test import TestCase

from posts.models import Post


class PostModelTest(TestCase):
    def set_up(self):
        Post.objects.create(
            test='test'
        )

    def test_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.test}'
        self.assertEqual(expected_object_name, 'test')
