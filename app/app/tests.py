from django.test import TestCase
from app.calc import add, subtract


class CalsTests(TestCase):
    """Add two numbers together and return the result"""
    def test_add_numbers(self):
        self.assertEqual(add(3, 8), 11)

    """Subtract x from y and return result"""
    def test_subtract_numbers(self):
        self.assertEqual(subtract(5, 11), 6)
