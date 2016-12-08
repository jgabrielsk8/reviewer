from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from core.models import Company
from reviews.models import Review


class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.company = Company.objects.create(name='Test company')
        self.tester1 = User.objects.create_user(username='tester1', email='tester1@mail.com', password='123')
        self.tester2 = User.objects.create_user(username='tester2', email='tester2@mail.com', password='123')

    def tearDown(self):
        self.company.delete()

    def test_only_authenticated_users_can_post_reviews(self):
        response = self.client.post(reverse('reviews:reviews'), {
            'company': self.company,
            'title': 'Title',
            'summary': 'summary',
            'rating': 1
        })
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_only_authenticated_users_can_see_reviews(self):
        response = self.client.get(reverse('reviews:reviews'))
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_user_can_see_others_reviews(self):
        self.client.login(username='tester1', password='123')
        Review.objects.create(company=self.company, title='Testing ownership',
                              summary='No other user can see this but me', rating=5,
                              reviewer=self.tester2)

        reviews_count = Review.objects.all().count()
        response = self.client.get(reverse('reviews:reviews'))
        user_reviews_count = len(response.data)

        self.assertNotEqual(reviews_count, user_reviews_count)

    def test_user_can_see_his_reviews(self):
        self.client.login(username='tester1', password='123')
        Review.objects.create(company=self.company, title='Testing ownership',
                              summary='Only I can see this', rating=5,
                              reviewer=self.tester1)

        reviews_count = Review.objects.all().count()
        response = self.client.get(reverse('reviews:reviews'))
        user_reviews_count = len(response.data)

        self.assertEqual(reviews_count, user_reviews_count)

    def test_rating_in_range(self):
        data = {
            'company': self.company.pk,
            'title': 'Testing ownership',
            'summary': 'Only I can see this',
            'rating': 6,
        }

        self.client.login(username='tester1', password='123')

        response = self.client.post(reverse('reviews:reviews'), data)

        self.assertEqual(response.data, {'rating': ['Ratings must be in range from 1 through 5.']})

    def test_title_in_range(self):
        data = {
            'company': self.company.pk,
            'title': 'Testing ownership' * 100,
            'summary': 'Only I can see this',
            'rating': 5,
        }

        self.client.login(username='tester1', password='123')

        response = self.client.post(reverse('reviews:reviews'), data)

        self.assertEqual(response.data, {'title': ['Ensure this field has no more than 64 characters.']})

    def test_summary_in_range(self):
        data = {
            'company': self.company.pk,
            'title': 'Testing ownership',
            'summary': 'Only I can see this' * 10000,
            'rating': 5,
        }

        self.client.login(username='tester1', password='123')

        response = self.client.post(reverse('reviews:reviews'), data)

        self.assertEqual(response.data, {'summary': ['Ensure this field has no more than 10000 characters.']})
