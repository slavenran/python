class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2*self.width + 2*self.height

    def get_diagonal(self):
        return (self.width**2 + self.height**2)**.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        shape = ''
        for i in range(self.height):
            shape += '*'*self.width + '\n'
        return shape

    def get_amount_inside(self, shape):
        return (self.width//shape.width) * (self.height//shape.height)

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side
    
    def __str__(self):
        return f'Square(side={self.width})'


rect = Rectangle(4, 8)
rect2 = Rectangle(3, 6)

sqr = Square(4)

print(rect, sqr, rect.get_diagonal())
print(rect.get_picture())
print(sqr.get_picture())
print(rect.get_amount_inside(rect2))