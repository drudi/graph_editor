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

    def test_set_pixel(self):
        c = Canvas(3, 3)
        c.set_pixel(1, 1, 'W')
        self.assertEqual('W', c.area[1][1])
        with self.assertRaises(IndexError):
            c.set_pixel(5, 5, 'W')

    def test_clear_canvas(self):
        c = Canvas(3, 3)
        for i in range(3):
            for j in range(3):
                c.set_pixel(j, i, 'W')
        c.clear_canvas()
        expected = [['O','O','O'],['O','O','O'],['O','O','O']]
        self.assertEqual(expected, c.area)
