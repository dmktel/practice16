'''
Напишите код для описания геометрической фигуры.
Создайте класс «прямоугольник» с помощью метода 
 __init__(). На выходе в консоли вам необходимо 
 получить длину и ширину с итоговыми значениями. 
'''

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

# rectangle parameters and area return
    def get_area(self):
        return f'Length: {self.length}, width: {self.width}, area: {self.length * self.width}'
