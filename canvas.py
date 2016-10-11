#! /usr/bin/env python3

class Canvas:
    def __init__(self, m, n):
        self.area = [['O' for i in range(n)] for i in range(m)]

    def set_pixel(self, y, x, value):
        self.area[y][x] = value

    def clear_canvas(self):
        for i in range(len(self.area)):
            for j in range(len(self.area[0])):
                self.area[i][j] = 'O'
