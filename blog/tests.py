from blog.models import Post
from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone


class PostTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        Post.objects.create(author_id=user.id,
                            title="Coringa",
                            subtitle="Uxe 1",
                            text="hahahahahaha ...")
        Post.objects.create(author_id=user.id,
                            title="A lagoa azul",
                            subtitle="Uxe 2",
                            text="a lagoa azul ...")

    def test_text_from_title(self):
        """Post - get title check text"""
        post_1 = Post.objects.get(title="Coringa")
        post_2 = Post.objects.get(title="A lagoa azul")
        self.assertEqual(post_1.text, "hahahahahaha ...")
        self.assertEqual(post_2.text, "a lagoa azul ...")

    def test_title_from_text(self):
        """Post - get text check title"""
        post_1 = Post.objects.get(text="hahahahahaha ...")
        post_2 = Post.objects.get(text="a lagoa azul ...")
        self.assertEqual(post_1.title, "Coringa")
        self.assertEqual(post_2.title, "A lagoa azul")

    def test_title_from_subtitle(self):
        """Post - get text check subtitle"""
        post_1 = Post.objects.get(subtitle="Uxe 1")
        post_2 = Post.objects.get(subtitle="Uxe 2")
        self.assertEqual(post_1.title, "Coringa")
        self.assertEqual(post_2.title, "A lagoa azul")

    def tearDown(self):
        post_1 = Post.objects.get(title="Coringa")
        post_1.delete()
        post_2 = Post.objects.get(title="A lagoa azul")
        post_2.delete()
        user = User.objects.get(username='testuser')
        user.delete()
