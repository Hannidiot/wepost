from django.test import TestCase


class TestPageTest(TestCase):

    def test_page_returns_correct_html(self):
        response = self.client.get('/wepost/test/')
        html = response.content.decode('utf8')

        self.assertIn("A Test Page appears", html)
        self.assertTemplateUsed(response, 'wepost_main/test.html')
