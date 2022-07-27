# 61 - Refaça o desafio 51 , lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

from time import sleep

a1 = float(input("Primeiro termo da PA: "))
print("")
r = float(input("Razão da PA: "))
print('')

print("A seguir os 10 primeiros termos da PA!!!")
print('')

count = int(0)

while count<10:
    sleep(0.2)
    print(f'{a1:.1f}')
    a1 += r
    count += 1 
    
print('FIM do PROGRAMA!!!')
