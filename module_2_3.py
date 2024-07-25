my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
indeks = 0
while indeks < len(my_list):
    element_spiska = my_list[indeks]
    indeks = indeks + 1
    if element_spiska > 0:
        print(element_spiska)
    elif element_spiska < 0:
        break
    else:
        continue
