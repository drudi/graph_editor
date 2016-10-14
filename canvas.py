#! /usr/bin/env python3

class Canvas:
    def __init__(self, m, n):
        self.area = [['O' for i in range(m)] for i in range(n)]

    def _check_swap(self, var1, var2):
        if var1 > var2:
            tmp = var1
            var1 = var2
            var2 = tmp
        return (var1, var2)

    def set_pixel(self, x, y, value):
        self.area[y][x] = value

    def clear_canvas(self):
        for i in range(len(self.area)):
            for j in range(len(self.area[0])):
                self.area[i][j] = 'O'

    def vertical_line(self, column, begin_line, end_line, color):
        begin_line, end_line = self._check_swap(begin_line, end_line)
        for i in range(begin_line, end_line + 1):
            self.area[i][column] = color

    def horizontal_line(self, begin_column, end_column, line, color):
        begin_column, end_column = self._check_swap(begin_column, end_column)
        for i in range(begin_column, end_column + 1):
            self.area[line][i] = color

    def rectangle(self, ul_x, ul_y, br_x, br_y, color):
        for i in range(ul_x, br_x + 1):
            for j in range(ul_y, br_y + 1):
                self.area[j][i] = color

    def paint_region(self, x, y, color):
        original_color = self.area[y][x]
        self._color_fill(y, x, original_color, color)

    def _color_fill(self, row, col, original_color, new_color):
        if row < 0 or row > len(self.area) - 1:
            return None
        if col < 0 or col > len(self.area[0]) - 1:
            return None
        if self.area[row][col] != original_color:
            return None
        self.area[row][col] = new_color
        self._color_fill(row + 1, col, original_color, new_color)
        self._color_fill(row - 1, col, original_color, new_color)
        self._color_fill(row, col - 1, original_color, new_color)
        self._color_fill(row, col + 1, original_color, new_color)
