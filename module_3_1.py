calls = 0
def count_calls():
    global calls
    calls = calls + 1
    return calls
def string_info(string):
    count_calls()
    Dlina_str  = len(string)
    Verh_registr = string.upper()
    Nizhniy_registr = string.lower()
    Kortezh = Dlina_str, Verh_registr, Nizhniy_registr,
    return Kortezh

def is_contains(string, list_to_search = []):
    count_calls()
    string = string.upper()
    list_to_search = [s.upper() for s in list_to_search]
    result1 = string in list_to_search

    return result1

print(string_info('stRoka'))
print(string_info('stRok'))
print(string_info('stRo'))
print(string_info('stR'))

print(is_contains('Dima', ['Msrina', 'Masha', 'Nikita']))
print(is_contains('Dima', ['Msrina', 'Nikita', 'dima']))
print(is_contains('Dima', ['Msrina', 'Dima', 'Nikita']))

print(calls)






