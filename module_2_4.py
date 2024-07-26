numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers: #Цикл переборки значений списка
    is_prime = True
    if i == 1:
        continue       #исключение единицы из простых и составных чисел
    for j in range(2, numbers[i-1]): #цикл проверки числа
        if i % j == 0:
            is_prime = False
            break
        else:
            continue
    if is_prime: #запись числа в соответстыующий список
        primes.append(i)
    else:
        not_primes.append(i)
print(primes)
print(not_primes)
