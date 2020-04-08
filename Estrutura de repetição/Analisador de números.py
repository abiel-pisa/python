r = 's'
s = 0
cont = 0
n=0
maior = 0
while r != 'n':
    n = int(input('Digite um número: '))
    r = str(input('Quer continhuar[s/n]: ')).strip().lower()[0]
    s += n
    cont += 1
    if n > maior:
        maior = n
    if cont == 1:
        menor = n
    if n < menor:
        menor = n

media= s/cont
print('A média destes números é {}'.format(media))
print('O maior número foi {}'. format(maior))
print('O menor número foi {}'.format(menor))