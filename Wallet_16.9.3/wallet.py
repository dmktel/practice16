'''
В проекте «Дом питомца» скоро появится новая
 услуга: электронный кошелек. То есть система
  будет хранить данные о своих клиентах и об
   их финансовых операциях. 

Вам нужно написать программу, обрабатывающую
 данные, и на выходе в консоль получить следующее:
  Клиент "Иван Петров". Баланс: 50 руб.
'''
class User:
    def __init__(self, name='', amount=0) -> None:
        self.name = name
        self.amount = amount

# get data user amount
    def get_amount(self, user_dict):
        self.name = user_dict.get('name')
        self.amount = user_dict.get('amount')