class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b


rec = Rectangle(3, 5)
print(f'Area of the Rectangle is {rec.area()}')
