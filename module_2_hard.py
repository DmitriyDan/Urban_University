for n in range(3,21):
    cod = ''
    for i in range(1,n):
        for j in range(i+1,n):
            if n % (i+j) == 0:
                cod += f'{i}{j}'
    print(f'{n} - {cod}')



