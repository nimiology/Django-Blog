from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APITestCase

from projects.models import Project


def UserToken(username):
    user = User(username=username, password='1234')
    user.save()
    refresh = RefreshToken.for_user(user)
    return user, f'Bearer {refresh.access_token}'


class ProjectAPITest(APITestCase):
    def test_create_project(self):
        user, tokenUser = UserToken('testman')
        request = self.client.post(reverse('projects:project_api:create_project'),
                                   HTTP_AUTHORIZATION=tokenUser,
                                   data={'title': 'test',
                                         'github': 'https://github.com/nimiology',
                                         'text': 'test',
                                         'publish': True})
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_get_project(self):
        project = Project(title='test', publish=True,
                          github='https://google.com/')
        project.save()
        request = self.client.get(reverse('projects:project_api:project',
                                          args=(project.pk,)))
        self.assertEqual(request.json()['id'], project.pk)

    def test_get_projects(self):
        request = self.client.get(reverse('projects:project_api:projects'))
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_put_project(self):
        user, tokenUser = UserToken('testman')
        project = Project(title='test', publish=True,
                          github='https://google.com/')
        project.save()
        request = self.client.put(reverse('projects:project_api:project',
                                          args=(project.pk,)),
                                  HTTP_AUTHORIZATION=tokenUser,
                                  data={'title': 'test',
                                        'github': 'https://github.com/nimiology',
                                        'text': 'test',
                                        'publish': True})
        self.assertEqual(request.json()['id'], project.pk)

    def test_delete_project(self):
        user, tokenUser = UserToken('testman')
        project = Project(title='test', publish=True,
                          github='https://google.com/')
        project.save()
        request = self.client.delete(reverse('projects:project_api:project',
                                             args=(project.pk,)),
                                     HTTP_AUTHORIZATION=tokenUser,
                                     )
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
