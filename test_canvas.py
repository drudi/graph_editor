from unittest import TestCase
from canvas import Canvas


class TestEditorGrafico(TestCase):
    def test_create_empty_matrix(self):
        expected = [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]
        c = Canvas(3, 3)
        self.assertEqual(expected, c.area)

        c = Canvas(3, 4)
        expected.append(['O', 'O', 'O'])
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
        expected = [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]
        self.assertEqual(expected, c.area)

    def test_vertical_line(self):
        c = Canvas(4, 4)
        expected = [['O', 'O', 'O', 'O'],
                    ['O', 'W', 'O', 'O'],
                    ['O', 'W', 'O', 'O'],
                    ['O', 'O', 'O', 'O']]
        c.vertical_line(1, 1, 2, 'W')
        self.assertEqual(expected, c.area)
        d = Canvas(4, 4)
        d.vertical_line(1, 2, 1, 'W')
        self.assertEqual(expected, d.area)

    def test_horizontal_line(self):
        c = Canvas(4, 4)
        expected = [['O', 'O', 'O', 'O'],
                    ['O', 'W', 'W', 'O'],
                    ['O', 'O', 'O', 'O'],
                    ['O', 'O', 'O', 'O']]
        c.horizontal_line(1, 2, 1, 'W')
        self.assertEqual(expected, c.area)
        d = Canvas(4, 4)
        d.horizontal_line(2, 1, 1, 'W')
        self.assertEqual(expected, d.area)

    def test_draw_rectangle(self):
        expected = [['O', 'O', 'O', 'O'],
                    ['W', 'W', 'W', 'O'],
                    ['W', 'W', 'W', 'O'],
                    ['W', 'W', 'W', 'O']]
        c = Canvas(4, 4)
        c.rectangle(0, 1, 2, 3, 'W')
        self.assertEqual(expected, c.area)

    def test_paint_region(self):
        expected = [['O', 'O', 'O', 'O'],
                    ['W', 'W', 'W', 'O'],
                    ['O', 'W', 'W', 'W'],
                    ['X', 'O', 'W', 'O']]
        c = Canvas(4, 4)
        c.set_pixel(0, 3, 'X')
        c.set_pixel(2, 3, 'X')
        c.horizontal_line(0, 2, 1, 'X')
        c.horizontal_line(1, 3, 2, 'X')
        c.paint_region(1, 1, 'W')
        self.assertEqual(expected, c.area)

    def test_paint_only_one_pixel(self):
        expected = [['O', 'O'],
                    ['W', 'O']]
        c = Canvas(2, 2)
        c.set_pixel(0, 1, 'X')
        c.paint_region(0, 1, 'W')
        self.assertEqual(expected, c.area)
