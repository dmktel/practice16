'''
Создайте класс любых геометрических фигур, где на 
выход мы получаем характеристики фигуры. Каждый
 экземпляр должен иметь атрибуты, которые зависят
  от выбранной фигуры. Например, для прямоугольника
   это будут аргументы x, y, width и height.

Кроме того вы должны иметь возможность передавать
 эти атрибуты при создании объекта класса.

Создайте метод, который возвращает атрибуты
 вашей фигуры в виде строки. 
'''

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

# rectangle parameters return
    def get_rectangle(self):
        return f'Rectangle({self.x}, {self.y}, {self.width}, {self.height})'

class Circle:
    def __init__(self, r):
        self.r = r
# circle parameters return
    def get_circle(self):
        return f'Circle({self.r})'