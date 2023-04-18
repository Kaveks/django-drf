from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase,APIClient
from Blog.models import Post, Category
from django.contrib.auth.models import User


# Create your tests here.

class PostTests(APITestCase):

    def test_view_posts(self):
        """
        Ensure we can view all objects.
        """
        url = reverse('Blog_api:listCreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_account(self):
        """
        Ensure we can create a new Post object and view object.
        """
        self.test_category = Category.objects.create(name='django')

        self.testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')

        data = {"title": "new", "author": 1,
                "excerpt": "new", "content": "new"}
        url = reverse('Blog_api:listCreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 6)
        root = reverse(('Blog_api:detailCreate'), kwargs={'pk': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_update(self):
        client=APIClient()
        self.test_category = Category.objects.create(name='django')
        self.testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')
        self.testuser2 = User.objects.create_user(
            username='test_user2', password='123456789')
        test_post = Post.objects.create(
            category_id=1, title='Post Title', excerpt='Post Excerpt', content='Post Content', slug='post-title', author_id=2, status='published')
        client.login(username=self.testuser2.username, password=('123456789'))
        url = reverse(('Blog_api:detailCreate'), kwargs={'pk': 2})
        Content={
                    "id": 2,
                    "title": "Django rest framework",
                    "author": 2,
                    "excerpt": "Django REST framework is a powerful and flexible toolkit for building Web APIs.",
                    "content": "The Web browsable API is a huge usability win for your developers.\r\n    Authentication policies including packages for OAuth1a and OAuth2.\r\n    Serialization that supports both ORM and non-ORM data sources.\r\n    Customizable all the way down - just use regular function-based views if you don't need the more powerful features.\r\n    Extensive documentation, and great community support.\r\n    Used and trusted by internationally recognized companies including Mozilla, Red Hat, Heroku, and Eventbrite.",
                    "status": "published"
                }
        
        response=client.put(url, Content,format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)