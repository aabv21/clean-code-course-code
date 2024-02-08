class Point:
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

class Rectangle:
    def __init__(self, origin, width, height):
        self.origin = origin
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def print(self):
        top_right = self.origin.coord_x + self.width
        bottom_left = self.origin.coord_y + self.height
        print('Starting Point (X)): ' + str(self.origin.coord_x))
        print('Starting Point (Y)): ' + str(self.origin.coord_y))
        print('End Point X-Axis (Top Right): ' + str(top_right))
        print('End Point Y-Axis (Bottom Left): ' + str(bottom_left))


def build_rectangle():
    origin_point = Point(50, 100)
    rect = Rectangle(origin_point, 90, 10)

    return rect


rectangle = build_rectangle()

print(rectangle.area())
rectangle.print()
