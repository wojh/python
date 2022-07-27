#58 - Melhore o jogo do desafio 028 onde o computador vai pensar em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

print("""Você escolherá um número de 0 a 10 e o computador escolherá outro!!! 
Tente adivinhar qual o computador pensou!!!""")
print('')
sleep (2)

num_user = int(input("Insira seu número: "))
count = int(1)
num_comp = int(randint(0, 10))
print(f'Computador pensou em: {num_comp}')
print('')

while num_user != num_comp:
    num_user = int(input("Insira seu número novamente: "))
    num_comp = int(randint(0, 10))
    print(f'Computador pensou em: {num_comp}')
    print('')
    count += 1

if num_user == num_comp:
    print("Parabéns!!! Você adivinhou o número que o computador 'pensou'!!!")
    print(f"E você tentou {count} vezes até acertar!!!")
 
