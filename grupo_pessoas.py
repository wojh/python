#56 - Programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#⇒ A média da idade do grupo;
#⇒ Nome do homem mais velho;
#⇒ Quantas mulheres tem menos de 20 anos

total = int(0)
count = int(0)
man = ''
man_young = int(0)

for c in range(1, 5):
    name = input(f'Nome da pessoa {c}: ')
    genero = input(f'Genero da pessoa {c} (M/F): ').lower()
    if genero == 'f':
        idade = float(input('Idade da pessoa {}: ' .format(c)))
        if idade < 20:
            count += 1
    elif genero == 'm':
        idade = int(input('Idade da pessoa {}: ' .format(c)))
        if man_young < idade:
            man = name
    print('')
    
    total += idade
    
print(f'Média da idade do grupo: {total/4}')
print(f'Número de Mulheres com menos de 20 anos: {count} ')
if man == '':
    print('Não há homens no grupo')
else:
    print(f'Nome do homem mais velho: {man}')











