from rectangle import Rectangle, Square, Circle

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)
square_1 = Square(5)
square_2 = Square(10)
circle_1 = Circle(4)


figures = [rect_1, rect_2, square_1, square_2, circle_1]
for f in figures:
    if isinstance(f,Square):
        print(f.get_area_square())
    elif isinstance(f, Circle):
        print(f.get_area_circle())
    else:
        print(f.get_area())
