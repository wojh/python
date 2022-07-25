#52 -  Programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Tecle um número inteiro maior que 1: '))
print('')

tot = 0

if num <= 0:
    print('Número Inválido!!!')
elif num ==1:
    print('Deve ser maior que 1.')
else:
    for c in range(1, num+1):
        if num%c==0:
            tot += 1
    if tot == 2:
        print(f'SIM!!! {num} é primo!!!')
    else:
        print(f"Não!!! {num} não é primo!!!")









