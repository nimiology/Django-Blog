from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from projects.api.tests import UserToken
from staticpages.models import Message


class MessageAPITest(APITestCase):
    def test_create_message(self):
        request = self.client.post(reverse('staticpages:api:create_message'),
                                   data={'name': 'test',
                                         'email': 'test@test.com',
                                         'text': 'test'})
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_get_message(self):
        user, tokenUser = UserToken('testman')
        message = Message.objects.create(name='test', text='test',
                                         email='test@test.com')
        request = self.client.get(reverse('staticpages:api:message',
                                          args=(message.pk,)),
                                  HTTP_AUTHORIZATION=tokenUser,)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_permission_get_message(self):
        message = Message.objects.create(name='test', text='test',
                                         email='test@test.com')
        request = self.client.get(reverse('staticpages:api:message',
                                          args=(message.pk,)))
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, request.status_code)

    def test_permission_get_messages(self):
        request = self.client.get(reverse('staticpages:api:messages',))
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, request.status_code)

    def test_get_messages(self):
        user, tokenUser = UserToken('testman')
        request = self.client.get(reverse('staticpages:api:messages'),
                                  HTTP_AUTHORIZATION=tokenUser,)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_delete_project(self):
        user, tokenUser = UserToken('testman')
        message = Message.objects.create(name='test', text='test',
                                         email='test@test.com')
        request = self.client.delete(reverse('staticpages:api:message',
                                             args=(message.pk,)),
                                     HTTP_AUTHORIZATION=tokenUser,)
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
