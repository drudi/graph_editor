#! /usr/bin/env python3

class Canvas:
    def __init__(self, m, n):
        self.area = [['O' for i in range(n)] for i in range(m)]
