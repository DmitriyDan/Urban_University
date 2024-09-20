def add_everything_up(a, b):
    try:
        rezult = a + b
    except TypeError:
        rezult = str(a) + str(b)
    return rezult

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))




