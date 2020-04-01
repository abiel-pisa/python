idade_total = 0
at = 0
Hvelho = 0
cont = 0
i = 0
for c in range (0,4):
    nome = str(input('Digite seu nome:')).title()
    idade = int(input('Digite sua idade:'))
    sexo = str(input('Digite seu sexo:')).lower().strip()
    idade_total += idade
    if idade > at and sexo == 'masculino':
        Hvelho = nome
        i = idade
    if idade < 20 and sexo == 'feminino':
        cont += 1
    at =idade

media = idade_total/4
print('A média das idades é {} anos'.format(media))
if Hvelho != 0:
    print('O homem mais velho entre estes 4 é o sr.{} e têm {} anos'.format(Hvelho, i))
print('{} mulheres tem menos de 20 anos'.format(cont))