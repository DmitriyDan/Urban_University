immutable_var = 'odin', 2, 'tri', 4, True
print('Кортеж: ', immutable_var)
# immutable_var[0] = 1
# Кортеж относится  к неизменяемым типам данных. Поэтому изменить элемент
# кортежа на другое значение не получиться.
mutable_list = ['odin', 2, 'tri', 4, True]
print('Список: ',mutable_list)
mutable_list[0] = 1
mutable_list[4] = 5
mutable_list.append(6)
print('Измененный список: ', mutable_list)