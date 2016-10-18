"""Input validator for the graphic editor"""


class IndexValidator(object):
    """
    Input validator class to verify if the input commands honors
    the boundaries of the paint area
    """

    def __init__(self, area):
        self.height = len(area)
        self.width = len(area[0])

    def validate(self, direction, value):
        if direction == 'vertical' and (value < 0 or value > self.height):
            raise IndexError('Vertical index {0} out of bounds'.format(value))
        if direction == 'horizontal' and (value < 0 or value > self.width):
            raise IndexError(
                    'Horizontal index {0} out of bounds'.format(value))


class LimitValidator(object):
    """
    Input validator for the paint area
    """

    def validate(self, width, height):
        if (not isinstance(width, int) or
                width < 0 or
                not isinstance(height, int) or
                height < 0):
            raise ValueError('Dimensions must be positive integers')
