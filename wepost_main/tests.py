from django.test import TestCase


class TestPageTest(TestCase):

    def test_page_returns_correct_html(self):
        response = self.client.get('/wepost/test/')

        self.assertContains(response, "A Test Page appears")
        self.assertTemplateUsed(response, 'wepost_main/test.html')


class BasePageTest(TestCase):
    
    def setUp(self):
        self.response = self.client.get('/wepost/home/')

    def test_default_title(self):
        self.assertContains(self.response, 'Wepost - Post Your Life Moments')

    def test_default_content(self):
        self.assertContains(self.response, 'Place body content here!')


class ExploreTest(TestCase):

    def test_page_returns_correct_html(self):
        response = self.client.get('/wepost/explore/')
        self.assertTemplateUsed(response, 'wepost_main/explore.html')

    def test_navbar_show_correctly(self):
        response = self.client.get('/wepost/explore/')

        self.assertContains(response, "nav")
        self.assertContains(response, "Wepost")

        self.assertContains(response, "Login")
