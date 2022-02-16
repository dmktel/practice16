from wallet import User

users = [
    {'name': 'Иван Петров', 'amount': 50},
    {'name': 'Петр Сидоров', 'amount': 100}]

for user in users:
    result = User()
    result.get_amount(user) 
    print(f'Клиент "{result.name}". Баланс: {result.amount}')
