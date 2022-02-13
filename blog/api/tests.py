from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from blog.models import Tag, Category, Article, Section
from projects.api.tests import UserToken


class TagAPITest(APITestCase):
    def test_create_tag(self):
        user, tokenUser = UserToken('testman')
        request = self.client.post(reverse('blog:api:create_tag'),
                                   HTTP_AUTHORIZATION=tokenUser,
                                   data={'title': 'test',
                                         'slug': 'test'})
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_get_tag(self):
        tag = Tag.objects.create(title='test', slug='test')
        request = self.client.get(reverse('blog:api:tag', args=(tag.pk,)))
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_edit_tag(self):
        tag = Tag.objects.create(title='test', slug='test')
        user, tokenUser = UserToken('testman')
        request = self.client.put(reverse('blog:api:tag', args=(tag.pk,)),
                                  HTTP_AUTHORIZATION=tokenUser,
                                  data={'title': 'test2',
                                        'slug': 'test'}
                                  )
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_delete_tag(self):
        tag = Tag.objects.create(title='test', slug='test')
        user, tokenUser = UserToken('testman')
        request = self.client.delete(reverse('blog:api:tag', args=(tag.pk,)),
                                     HTTP_AUTHORIZATION=tokenUser, )
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_tags(self):
        request = self.client.get(reverse('blog:api:tags'))
        self.assertEqual(request.status_code, status.HTTP_200_OK)


class CategoryAPITest(APITestCase):
    def test_create_category(self):
        user, tokenUser = UserToken('testman')
        request = self.client.post(reverse('blog:api:create_category'),
                                   HTTP_AUTHORIZATION=tokenUser,
                                   data={'title': 'test',
                                         'slug': 'test'})
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_get_category(self):
        category = Category.objects.create(title='test', slug='test')
        request = self.client.get(reverse('blog:api:category', args=(category.pk,)))
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_edit_category(self):
        category = Category.objects.create(title='test', slug='test')
        user, tokenUser = UserToken('testman')
        request = self.client.put(reverse('blog:api:category', args=(category.pk,)),
                                  HTTP_AUTHORIZATION=tokenUser,
                                  data={'title': 'test2',
                                        'slug': 'test'}
                                  )
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_delete_category(self):
        category = Category.objects.create(title='test', slug='test')
        user, tokenUser = UserToken('testman')
        request = self.client.delete(reverse('blog:api:category', args=(category.pk,)),
                                     HTTP_AUTHORIZATION=tokenUser, )
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_categories(self):
        request = self.client.get(reverse('blog:api:categories'))
        self.assertEqual(request.status_code, status.HTTP_200_OK)


class ArticleAPITest(APITestCase):
    def test_create_article(self):
        user, tokenUser = UserToken('testman')
        request = self.client.post(reverse('blog:api:create_article'),
                                   HTTP_AUTHORIZATION=tokenUser,
                                   data={'title': 'test',
                                         'slug': 'test',
                                         'thumbnail': open('static/assets/img/404.jpg', 'rb')})
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_get_article(self):
        article = Article.objects.create(title='test', slug='test', published=True)
        request = self.client.get(reverse('blog:api:article', args=(article.slug,)))
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_edit_article(self):
        article = Article.objects.create(title='test', slug='test')
        user, tokenUser = UserToken('testman')
        request = self.client.put(reverse('blog:api:article', args=(article.slug,)),
                                  HTTP_AUTHORIZATION=tokenUser,
                                  data={'title': 'test2',
                                        'slug': 'test',
                                        'thumbnail': open('static/assets/img/404.jpg', 'rb')
                                        }
                                  )
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_delete_article(self):
        article = Article.objects.create(title='test', slug='test')
        user, tokenUser = UserToken('testman')
        request = self.client.delete(reverse('blog:api:article', args=(article.slug,)),
                                     HTTP_AUTHORIZATION=tokenUser, )
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_articles(self):
        request = self.client.get(reverse('blog:api:articles'))
        self.assertEqual(request.status_code, status.HTTP_200_OK)


class SectionAPITest(APITestCase):
    def setUp(self):
        self.article = Article.objects.create(title='test', slug='test', published=True)
    def test_create_section(self):
        user, tokenUser = UserToken('testman')
        request = self.client.post(reverse('blog:api:create_section'),
                                   HTTP_AUTHORIZATION=tokenUser,
                                   data={'title': 'test',
                                         'article': self.article.pk})
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_get_section(self):
        section = Section.objects.create(title='test', article=self.article)
        request = self.client.get(reverse('blog:api:section', args=(section.pk,)))
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_edit_section(self):
        section = Section.objects.create(title='test', article=self.article)
        user, tokenUser = UserToken('testman')
        request = self.client.put(reverse('blog:api:section', args=(section.pk,)),
                                  HTTP_AUTHORIZATION=tokenUser,
                                  data={'title': 'test2',
                                        'article': self.article.pk}
                                  )
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_delete_section(self):
        section = Section.objects.create(title='test', article=self.article)
        user, tokenUser = UserToken('testman')
        request = self.client.delete(reverse('blog:api:section', args=(section.pk,)),
                                     HTTP_AUTHORIZATION=tokenUser, )
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_sections(self):
        request = self.client.get(reverse('blog:api:sections'))
        self.assertEqual(request.status_code, status.HTTP_200_OK)


