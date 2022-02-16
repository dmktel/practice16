'''
Откройте сайт Дом питомца
 и на основе имеющихся в нем данных создайте 
 конструктор класса Cat со следующими параметрами:
  имя, пол, возраст.

В отдельный файл импортируйте и создайте объект Cat, который выводит имеющихся на сайте котов, с одинаковыми параметрами, но с разными значениями. 
'''
class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

# cat info output   
    def cat_info(self):
        return {'name': self.name, 'gender': self.gender, 'age': self.age}