from django.test import TestCase

from mainpage.models import URL

URLs = [
    'https://i.pinimg.com/originals/36/54/e7/3654e7e5cd4023d6a65bb172fb178be0.jpg',
    'https://cms.qz.com/wp-content/uploads/2017/03/01100014-e1490900522602.jpg?quality=75&strip=all&w=1600&h=900&crop=1'
]

class URLTestCase(TestCase):
    def setUp(self):
        URL.objects.create(original_url=URLs[0])
        URL.objects.create(original_url=URLs[0])
        URL.objects.create(original_url=URLs[1])

    def test_url_count(self):
        self.assertEqual(len(URL.objects.all()), 3)

    def test_duplicate_urls(self):
        self.assertEqual(len(URL.objects.filter(original_url=URLs[0])), 2)

    def test_empty_url(self):
        new_url = URL.objects.create()
        self.assertEqual(new_url.validate(), 'URL cannot be empty')