from gest import Gest

gests = [
    {'name': 'Иван Петров',
     'city': 'Москва',
      'status': 'Наставник'},
    {'name': 'Петр Сидоров',
     'city': 'Самара',
     'status': 'Администратор'},
     {'name': 'Павел Медведев',
     'city': 'Казань',
     'status': 'Докладчик'}
     ]

for gest in gests:
    result = Gest()
    result.get_gest_list(gest) 
    print(f'{result.name}, г.{result.city}, статус "{result.status}"')