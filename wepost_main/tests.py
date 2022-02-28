from django.test import TestCase


class TestPageTest(TestCase):

    def test_page_returns_correct_html(self):
        response = self.client.get('/wepost/test/')

        self.assertContains("A Test Page appears", response)
        self.assertTemplateUsed(response, 'wepost_main/test.html')


class BasePageTest(TestCase):
    
    def setUp(self):
        self.response = self.client.get('/wepost/home/')

    def test_default_title(self):
        self.assertContains('Wepost - Post Your Life Moments', self.response)

    def test_default_content(self):
        self.assertContains('Place body content here!', self.response)


class ExploreTest(TestCase):

    def test_page_returns_correct_html(self):
        response = self.client.get('/wepost/explore/')
        self.assertTemplateUsed(response, 'wepost_main/explore.html')

    def test_navbar_show_correctly(self):
        response = self.client.get('/wepost/explore/')

        self.assertContains("nav", response)
        self.assertContains("Wepost", response)

        self.assertContains("Login", response)
