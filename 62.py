# 61 - Refaça o desafio 51 , lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
a1 = float(input("Primeiro termo da PA: "))
r = float(input("Razão da PA: "))
print('')
print("Abaixo os 10 primeiros termos da PA!!!")
count = int(0)
while count<10:
    print(f'{a1:.1f}',end='   ')
    a1 += r
    count += 1 
    
print('\n')
r_s = input("Deseja mostrar mais termos da PA [s/n]: ").lower()
n = int(0)

while r_s == 's':
    n += int(input('Tecle quantos termos mais deseja: '))
    
    while count<(10 + n):
        print(f'{a1:.1f}',end='   ')
        a1 += r
        count += 1 
        if count == (10 + n):
            print('\n')
            r_s = input("Deseja mostrar mais termos da PA [s/n]: ").lower()
             
print('')
print('FIM do PROGRAMA!!!')
