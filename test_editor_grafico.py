from unittest import TestCase
from canvas import Canvas

class TestEditorGrafico(TestCase):
    def test_create_empty_matrix(self):
        expected = [['O','O','O'],['O','O','O'],['O','O','O']]
        c = Canvas(3, 3)
        self.assertEqual(expected, c.area)

        c = Canvas(4, 3)
        expected.append(['O','O','O'])
        self.assertEqual(expected, c.area)
