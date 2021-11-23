from django.test import TestCase
from django.urls import reverse, resolve

from Core.views import HomePageView


class HomePageViewTests(TestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_page_template(self):
        self.assertTemplateUsed(
            self.response, template_name='home/home.html'
        )

    def test_home_page_contains_text(self):
        self.assertContains(self.response, 'Home')

    def test_home_page_does_not_contains_text(self):
        self.assertNotContains(self.response, 'This is not is home page')

    def test_home_url_resolve_homepageview(self):
        view = resolve('/en/')
        self.assertEqual(
            view.func.__name__, HomePageView.as_view().__name__
        )
