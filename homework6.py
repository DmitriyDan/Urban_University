my_dict = {'Denis': 1985, 'ira': 1990, 'Zina': 1994}
print('Словарь: ', my_dict)
print('Значение ключа: ',my_dict['Denis'])
print('Значение отсутствующего ключа: ',my_dict.get('Vasya'))
my_dict.update({'Leonid': 1980, 'Serjey': 1983})
print('Плюс две пары: ',my_dict)
print('Удаление пары и вывод значения',my_dict.pop('ira'))
print('Словарь: ',my_dict)

my_set = {1, 2, 3, 4, 2, 1,'Лампа'}
print('Множество: ',my_set)
my_set.add(9)
my_set.add(45)
print('плюс два элемента: ',my_set)
my_set.discard(4)
print('Удалён один элемент: ',my_set)
