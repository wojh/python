#54 - Programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import datetime

ano_atual = datetime.datetime.now().year

maiores = int(0)

for c in range(1, 8):
    ano_nasc = int(input(f'Ano de nascimento da pessoa {c}: '))
    if (ano_atual - ano_nasc) > 18:
        maiores += 1
        
print('Pronto!!! Obrigado pelos dados fornecidos!!!')

if maiores == 0:
    print('Todos são menores de idade!!!')
elif (7-maiores == 0):
    print('Todos os {maiores}são maiores de idade!!!')
else:
    print(f"Assim, {maiores} são maiores de idade e {7-maiores} são menores de idade")













