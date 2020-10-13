class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point('{}', {}, {})".format(self.name, self.x, self.y)

    def __str__(self):
        return '{}({}, {})'.format(self.name, self.x, self.y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return self.x, self.y

    def __invert__(self):
        return Point(self.name, self.y, self.x)

if __name__ == '__main__':
    points = [Point('A', 0, 3), Point('B', 4, 0)]
    print(points)
    print(points[0])
    print(repr(points[0]))
