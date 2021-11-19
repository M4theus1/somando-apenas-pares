c = 0
n = 0
cont = 0
for c in range (1, 7):
    n = int(input('Por favor, digite o {} número: '.format(c)))
    if (n % 2) == 0:
        n = n + n
        cont = cont + 1
    else:
        n = 0

print('Você informou {} números PARES e a soma foi {}'.format(cont, n))
