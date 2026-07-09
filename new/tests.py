from django.test import TestCase
from .models import Category,Article,Tag

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category=Category.objects.create(name='Sport')

    def test_category(self):
        self.assertEqual(self.category.name,'Sport')
        self.assertNotEqual(self.category.name,'Mahalliy')

class TagModelTest(TestCase):

    def test_tag_creation(self):
        tag = Tag.objects.create(name="Dasturlash")

        self.assertEqual(tag.name, "Dasturlash")





