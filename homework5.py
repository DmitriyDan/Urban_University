immutable_var = 'odin', 2, 'tri', 4, True
print('Кортеж: ', immutable_var)
mutable_list = ['odin', 2, 'tri', 4, True]
print('Список: ',mutable_list)
mutable_list[0] = 1
mutable_list[4] = 5
mutable_list.append(6)
print('Измененный список: ', mutable_list)